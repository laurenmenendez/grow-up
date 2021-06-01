from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.child_views import Children, ChildDetail
from .views.milestone_views import Milestones, MilestoneDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('children/', Children.as_view(), name='children'),
    path('children/<int:pk>/', ChildDetail.as_view(), name='child_detail'),
    path('milestones/', Milestones.as_view(), name='milestones'),
    path('milestones/<int:pk>/', MilestoneDetail.as_view(), name='milestone_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
