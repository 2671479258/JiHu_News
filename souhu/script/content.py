# 添加 django 环境
import os, sys
import django

# 1. 找到当前项目的上一级目录
sys.path.insert(0, '../')
# 2. 在项目根目录中找到settings配置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'souhu.settings')
# 3. 该文件交给django运行
django.setup()

from news.models import News



def generic_detail_html(new):
    new_new1 = News.objects.exclude(detail__isnull=True).order_by('-id').first()


    new_new2 = News.objects.exclude(detail__isnull=True).order_by('-id')[1]  # 获取倒数第二个新闻对象
    new_new3 = News.objects.exclude(detail__isnull=True).order_by('-id')[2]  # 获取倒数第三个新闻对象
    new_new4 = News.objects.exclude(detail__isnull=True).order_by('-id')[3]  # 获取倒数第4个新闻对象
    new_new5 = News.objects.exclude(detail__isnull=True).order_by('-id')[4]  # 获取倒数第5个新闻对象
    new_new6 = News.objects.exclude(detail__isnull=True).order_by('-id')[5]  # 获取倒数第6个新闻对象

    context = {
        'new':new,
        'new_new1':new_new1,
        'new_new2':new_new2,
        'new_new3':new_new3,
        'new_new4':new_new4,
        'new_new5':new_new5,
        'new_new6':new_new6

    }

    # 1. 加载模板
    from django.template import loader
    detail_template = loader.get_template('content.html')
    # 2. 模板渲染
    detail_html_data = detail_template.render(context)
    # 3. 写入文件
    import os
    from souhu import settings

    file_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'front/news/%s.html' % new.id)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(detail_html_data)
        print(new.id)


# 1. 要进入到数据库查询所有的商品数据
news = News.objects.exclude(detail__isnull=True)
for new in news:
    generic_detail_html(new)

