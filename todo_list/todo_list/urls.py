from rest_framework.routers import DefaultRouter
from todo_app.views import TasklistViewSet

router = DefaultRouter()

app_name = "todo_app"


router.register(
    prefix="api/tasks",
    viewset=TasklistViewSet,
)

urlpatterns = router.urls
