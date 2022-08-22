from InstagramAPI.src.http.Response.Objects.HdProfilePicUrlInfo import HdProfilePicUrlInfo
from .Response import Response



class UsernameInfoResponse(Response):
    def __init__(self, response):

        self.usertags_count = None
        self.has_anonymous_profile_picture = None
        self.full_name = None
        self.following_count = None
        self.auto_expand_chaining = None
        self.external_lynx_url = ''
        self.can_boost_post = False
        self.hd_profile_pic_versions = None
        self.biography = None
        self.has_chaining = None
        self.media_count = None
        self.follower_count = None
        self.pk = None
        self.username = None
        self.geo_media_count = None
        self.profile_pic_url = None
        self.can_see_organic_insights = False
        self.is_private = None
        self.can_convert_to_business = False
        self.is_business = None
        self.show_insights_terms = False
        self.hd_profile_pic_url_info = None
        self.usertag_review_enabled = False
        self.external_url = None
        self.is_favorite = None
        self.is_verified = None

        if self.STATUS_OK == response['status']:
            self.full_name = response['user']['full_name']
            self.following_count = response['user']['following_count']
            
            self.follower_count = response['user']['follower_count']
            
            self.username = response['user']['username']

    def getFollowingCount(self):
        return self.following_count

    def getFollowerCount(self):
        return self.follower_count