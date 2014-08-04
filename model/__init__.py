from .model import *


def get_tags(tags):
    """将提交的tag字符串用分割符(,)打散为列表
    """
    if tags:
        tags = tags.replace('，', ',').rstrip(',')
        return tags.split(',')
    else:
        return []


def tag_save(tags, pid):
    """保存tags

    """
    #尝试删除所有已存在的tag
    try:
        post_tag = PostTag.delete().where(PostTag.post == pid)
        post_tag.execute()
    except DoesNotExist:
        pass

    #标签列表不为空时
    if tags:
        for tag in tags:
            try:
                t = Tag.get(Tag.tag == tag)
            except DoesNotExist:
                #插入时只截取前25个字符
                t = Tag.create(tag=tag[:25])
            PostTag.create(tag=t.id, post=pid)


def get_tags_and_numbers():
    """获取标签和标签的数量

    """
    return Tag.select(Tag, fn.Count(Post.id).alias('count')).join(PostTag).join(Post).group_by(Tag)