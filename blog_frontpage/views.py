from django.views.generic import TemplateView, ListView, DetailView

from blog_frontpage.models import Post


# class based view for blog post
class PostView(DetailView):
    model = Post
    template_name = 'blog_front/post.html'


# class based view for blog
class BlogView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_front/blog.html'


# class based view for about
class AboutView(TemplateView):
    template_name = 'blog_front/about.html'


# class based view for contact
class ContactView(TemplateView):
    template_name = 'blog_front/contact.html'


# class based view for index
class IndexView(TemplateView):
    template_name = 'blog_front/index.html'
