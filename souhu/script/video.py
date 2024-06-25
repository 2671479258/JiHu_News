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

def generic_video_html(new):
    context = {
        'new': new,
    }
    # 1. 加载模板
    from django.template import loader
    detail_template = loader.get_template('video.html')
    # 2. 模板渲染
    detail_html_data = detail_template.render(context)
    # 3. 写入文件
    import os
    from souhu import settings

    file_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'front/v_news/%s.html' % new.id)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(detail_html_data)
        print(new.id)

# 1. 要进入到数据库查询所有的商品数据
news = News.objects.exclude(video_detail__isnull=True)
for new in news:
    generic_video_html(new)
