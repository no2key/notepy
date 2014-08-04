$(document).ready(function () {
    /**
     *  获取cookie
     */
    var getCookie = function (name) {
        var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return r ? r[1] : undefined;
    }
    /**
     * 添加文章
     */
    var addPost = function () {
        var text = $('.post-add, .post-update input:text');
        text.keydown(function(event){
            if (event.target.name == 'title') {
                var title = event.target;
                if (title.value.length <= 30) {
                    $('#title-message').html('<p class="text-info">还可以输入:' + (30 - title.value.length) + '个字</p>')
                } else {
                    title.value = title.value.substr(0, 30)
                }
            }
        })
    }

    /**
     * 删除文章
     */
    var deletePost = function () {
        var del = function () {
            $('.yes').click(function (event) {
                event.preventDefault();
                var $form = $("#delete"),
                    id = $form.find("input[name='id']").val(),
                    _xsrf = getCookie('_xsrf');
                var url = $form.attr("action");

                $.post(url, { id: id, _xsrf: _xsrf}, function (data) {
                    $(".post").replaceWith(data);
                    //延迟1秒之后跳转
                    setTimeout(function () {
                        location.href = "/"
                    }, 1500)

                });
            });

        };
        /**
         * 返回
         */
        var back = function () {
            $('.no').click(function () {
                location.reload();
            });
        }

        /**
         * 执行删除操作
         */
        $(".delete").click(function (event) {
            event.preventDefault();
            var url = $(this).attr('href');
            $(this).load(url, function () {
                //显示提示页面
                $('#myModal').modal('show')
                del();
                back();
            });
        });
    }

    var updatePost = function () {
        $(".post-update form").submit(function (event) {
            event.preventDefault();
            var $form = $(this),
                id = $form.find("input[name='id']").val(),
                title = $form.find("input[name='title']").val(),
                content = $form.find("textarea[name='content']").val(),
                tags = $form.find("input[name='tags']").val(),
                _xsrf = getCookie('_xsrf');
            var url = $form.attr("action");

            $.post(url, { id: id, title: title, content: content, tags: tags, _xsrf: _xsrf}, function (data) {
                $(".post-update").replaceWith(data);
                setTimeout(function () {
                    location.reload();
                }, 1500)
            });
        });
    }

    /**
     * 当前页码突出显示
     */
    var pageNav = function() {
        var paths = location.pathname.split('/');
        var id = paths[paths.length-1].match(/\d+/);
        var pageId = '#page-' + id;
        $(pageId).addClass('active');
    }

    var disqus_shortname = 'maguowei'; // required: replace example with your forum shortname

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function () {
        var s = document.createElement('script'); s.async = true;
        s.type = 'text/javascript';
        s.src = '//' + disqus_shortname + '.disqus.com/count.js';
        (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
    }());

    pageNav();
    addPost();
    deletePost();
    updatePost();
})