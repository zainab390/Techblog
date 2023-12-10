from flask import render_template, request, Blueprint
from techblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
def landing_page():
    return render_template('landing_page.html')


@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', title='Home', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')