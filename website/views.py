from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Post, Comment, db
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

@views.route('/post/<int:post_id>', methods=['GET', 'POST'])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    
    if request.method == 'POST' and current_user.is_authenticated:
        content = request.form['content']
        if content.strip():
            new_comment = Comment(content=content, user_id=current_user.id, post_id=post_id)
            db.session.add(new_comment)
            db.session.commit()
            flash('Bình luận đã được thêm!', 'success')
            return redirect(url_for('views.view_post', post_id=post_id))
        else:
            flash('Bình luận không thể để trống.', 'error')
    
    return render_template('view_post.html', user=current_user, post=post, comments=comments)

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

@views.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        flash('Bạn không có quyền chỉnh sửa bài viết này.', 'error')
        return redirect(url_for('views.dashboard'))
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Bài viết đã được cập nhật!', 'success')
        return redirect(url_for('views.dashboard'))
    
    return render_template('edit_post.html', user=current_user, post=post)