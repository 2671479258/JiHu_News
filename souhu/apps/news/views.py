from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from article.models import Articles
from news.models import News
from videos.models import News_video
class get_news(View):
    def get(self,request):
        news_record=News.objects.exclude(detail__isnull=True).order_by('-release_date')
        news_record_list = []


        for record in news_record:
            # 创建一个字典
            news_dict = dict(
                id=record.id,
                title=record.title,
                default_image=str(record.default_image),
                release_date=record.release_date,

            )
            news_record_list.append(news_dict)

        articless_record = Articles.objects.all().order_by('-release_date')
        articless_record_list = []

        for record in articless_record:
            # 创建一个字典
            articles_dict = dict(
                id=record.id,
                title=record.title,
                release_date=record.release_date,

            )
            articless_record_list.append(articles_dict)

            videos_record =News.objects.exclude(video_detail__isnull=True).order_by('-release_date')
            videos_record_list = []

            for record in videos_record:
                # 创建一个字典
                videos_dict = dict(
                    id=record.id,
                    title=record.title,
                    default_image=str(record.default_image),
                    release_date=record.release_date,

                )
                videos_record_list.append(videos_dict)









        return JsonResponse({'code': 0, 'errmsg': 'ok', 'Nrecords': news_record_list,'Arecords':articless_record_list,'Vrecords':videos_record_list})

from news.models import Comment
class GetComment(View):
    def get(self, request, new_id):
        comments = Comment.objects.filter(new_id=new_id).select_related('user')
        comment_list = []
        for comment in comments:
            # 查询每个评论对应的回复列表
            replies = Reply.objects.filter(comment=comment).select_related('user', 'receiver')
            reply_list = []
            for reply in replies:
                # 构建回复对象字典
                reply_dict = {
                    'id': reply.id,
                    'username': reply.user.username,
                    'profile': reply.user.profile,
                    'reply': reply.reply,
                    'release_date': reply.release_date.strftime('%Y-%m-%d %H:%M:%S'),
                    # 其他回复相关的属性
                }
                reply_list.append(reply_dict)
            # 构建评论对象字典，包含回复列表
            comment_dict = {
                'id': comment.id,
                'user_id': comment.user.id,
                'username': comment.user.username,
                'profile': comment.user.profile,
                'comment': comment.comment,
                'release_date': comment.release_date.strftime('%Y-%m-%d %H:%M:%S'),
                # 其他评论相关的属性
                'replies': reply_list  # 将回复列表添加到评论对象中
            }
            comment_list.append(comment_dict)

        return JsonResponse({"comments": comment_list, 'code': 200})
from users.models import User
from django.utils import timezone

class PublishComment(View):
    def get(self, request):
        username = request.GET.get('username')
        comment = request.GET.get('comment')
        new_Id=request.GET.get('newId')
        # 根据 username 查询对应的用户对象
        user = User.objects.filter(mobile=username).first()
        if user:
            user_id = user.id
        else:
            # 处理找不到用户的情况
            "找不到用户名"
            user_id = None
        print(user.id)
        # 创建新评论，并关联到用户
        # 获取当前时间
        current_time = timezone.localtime(timezone.now())

        # 创建评论并保存到数据库
        new_comment = Comment.objects.create(comment=comment, user_id=user_id, new_id=new_Id, release_date=current_time)


        return JsonResponse({'code': 0, 'username': username,})


class SearchView(View):
    def get(self, request):
        # 1. 接收参数 排序规则 分页数量 当前页数

        page_size = request.GET.get('page_size')  # 默认每页数量为 6
        page = request.GET.get('page')  # 默认当前页数为 1
        q = request.GET.get('q')
        print(q)

        # 2. 查询数据
        news = News.objects.filter(title__contains=q,video_detail__isnull=True).order_by('id')
        print(news.first())

        # 分页
        from django.core.paginator import Paginator

        # 每页的数据量
        paginator = Paginator(news, per_page=page_size)
        # 获取指定页面的数据
        page_news = paginator.page(page)
        #
        # 4. 将获取到的查询数据集转成列表数据
        new_list = []
        for new in page_news.object_list:
            new_list.append({
                'id': new.id,
                'title': new.title,

                'default_image': str(new.default_image)
            })

        print(new_list)
        # 5. 获取总页数
        total_num = paginator.num_pages

        # 6. 返回响应
        return JsonResponse({
            'code': 0,
            'errmsg': 'ok',
            'list': new_list,
            'count': total_num,
            'q':q
        })


from news.models import Reply
class PublishReply(View):
    def get(self, request):
        username = request.GET.get('username')
        receiver = request.GET.get('receiver')
        reply=request.GET.get('reply')
        comment_id=request.GET.get('comment_id')

        # 根据 username 查询对应的用户对象
        user = User.objects.filter(mobile=username).first()
        if user:
            user_id = user.id
        else:
            # 处理找不到用户的情况
            "找不到用户名"
            user_id = None

        receiver=User.objects.filter(username=receiver).first()
        if receiver:
            receiver_id = receiver.id
        else:
            # 处理找不到用户的情况
            "找不到接受者"
            receiver_id = None

        print(receiver_id)
        print(user_id)
        print(reply)
        print(comment_id)

        # # 创建新评论，并关联到用户
        # # 获取当前时间
        current_time = timezone.localtime(timezone.now())
        #
        # # 创建评论并保存到数据库
        new_reply = Reply.objects.create(
            user_id=user_id,
            release_date=current_time,
            reply=reply,
            receiver_id=receiver_id,
            comment_id=comment_id
        )

        return JsonResponse({'code': 0 })
