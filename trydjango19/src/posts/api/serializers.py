from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
        ]

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug',
    )

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model=Post
        fields=[
            'url',
            'user',
            'title',
            'content',
            'publish',
    ]

    # def get_user(self, obj):
    #     return str(obj.user.username)

class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'user',
            'image',
            'slug',
            'content',
            'html',
            'publish',
            'comments',
        ]
    def get_html(self, obj):
        return obj.get_markdown()

    # def get_user(self, obj):
    #     return str(obj.user.username)

    def get_image(self, obj):
        try:
           image = obj.image.url
        except:
            image=None
        return image
    
    def get_comments(self, obj):
        # content_type = obj.get_content_type
        # object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

"""
data = {
    "title":"Yeah buddy",
    "content":"New content",
    "publish":"2017-4-12",
    "slug": "yeah-buddy",
}

new_item = PostDetailSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""
