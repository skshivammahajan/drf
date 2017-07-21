from django.conf.urls import url
from snippets import views

urlpatterns = [
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    #     url(r'^snippets/$', views.SnippetList.as_view()),
    #     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    #     url(r'^users/$', views.UserList.as_view()),
    #     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    #     url(r'^$', views.api_root),
    #     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
    #         views.SnippetHighlight.as_view()),

]

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
