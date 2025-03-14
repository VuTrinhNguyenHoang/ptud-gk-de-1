from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Post, db
import random

views = Blueprint('views', __name__)

@views.route('/')
def home():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('home.html', user=current_user, posts=posts)

@views.route('/dashboard')
@login_required
def dashboard():
    user_posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.created_at.desc()).all()
    total_posts = len(user_posts)
    return render_template('dashboard.html', user=current_user, total_posts=total_posts, posts=user_posts)

@views.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', user=current_user, post=post)

@views.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image_url = f'https://picsum.photos/800/400?random={random.randint(1, 1000)}'
        new_post = Post(title=title, content=content, image_url=image_url, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        flash('Bài viết đã được tạo!', 'success')
        return redirect(url_for('views.home'))
    
    return render_template('create_post.html', user=current_user)