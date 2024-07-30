from rest_framework.routers import DefaultRouter
from apps.account.views import UserViewSet

from apps.company.views import (
    CompanyViewSet,
    IndustryViewSet
)

from apps.userprofile.views import (
    ProfileViewSet,
    EducationViewSet,
    ExperienceViewSet,
    SkillViewSet,
    SkilledUsersViewSet
)

from apps.jobs.views import (
    JobViewSet,
    ApplicationViewSet,
    JobSkillViewSet
)


from address.views import AddressViewSet  # Import the AddressViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet, basename='users')
router.register(r'profile', ProfileViewSet, basename='profiles')
router.register(r'education', EducationViewSet, basename='educations')
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'comapany', CompanyViewSet, basename='comapany')
router.register(r'industriy', IndustryViewSet, basename='industries')
router.register(r'skill', SkillViewSet, basename='skill')
router.register(r'user-skill', SkilledUsersViewSet, basename='user-skill')
router.register(r'job', JobViewSet, basename='job')
router.register(r'job-skill', JobSkillViewSet, basename='job-skill')
router.register(r'application', ApplicationViewSet, basename='application')

# Register the AddressViewSet with the router
router.register(r'address', AddressViewSet, basename='address')

# Now you have an endpoint for addresses in your API
