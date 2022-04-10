from app.views import frontend


def setup_routes(app):
    app.router.add_static('/js/', path='templates/client/js', name='index.js', show_index=True)
    app.router.add_static('/css/', path='templates/client/css', name='style.css', show_index=True)
    app.router.add_static('/font/', path='templates/client/font', name='font', show_index=True)
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/post', frontend.post)
