"""Queries behind the views. Part 2 of the lab happens in this file."""
from blog.models import Post


def posts_for_front_page():
    # The template walks `post.author` (FK) and `post.tags` (M2M) per post, so a
    # plain queryset fires one extra query per post (N+1). `select_related`
    # joins the author into the posts query, and `prefetch_related` fetches all
    # tag rows in a second query, caching them on every post: 2 queries total,
    # independent of the number of posts.
    return (
        Post.objects.filter(published=True)
        .select_related("author")
        .prefetch_related("tags")
        .order_by("-published_at")
    )
