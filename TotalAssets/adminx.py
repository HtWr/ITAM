import xadmin
from xadmin import views


class BaseSetting(object):
    """主题配置"""
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    site_title = 'Local IT'
    site_footer = 'CTU-Local IT'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)