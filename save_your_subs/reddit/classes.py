from dataclasses import dataclass
from datetime import datetime


example = {
    "approved_at_utc": None,
    "subreddit": "HentaiBondageTales",
    "selftext": "",
    "author_fullname": "t2_efnc4sfd",
    "saved": False,
    "mod_reason_title": None,
    "gilded": 0,
    "clicked": False,
    "is_gallery": True,
    "title": "A weekend at the beach",
    "link_flair_richtext": [],
    "subreddit_name_prefixed": "r/HentaiBondageTales",
    "hidden": False, "pwls": None,
    "link_flair_css_class": "",
    "downs": 0,
    "thumbnail_height": 103,
    "top_awarded_type": None,
    "hide_score": False,
    "media_metadata": {
        "v8dmkhn60vxa1": {
            "status": "valid",
            "e": "Image",
            "m": "image/png",
            "o": [{"y": 1704, "x": 2316, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=1080&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=e155368b6df7348e6aa5e259c7f203c405fd5514"}],
            "p": [
                {"y": 79, "x": 108, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=108&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=55e53e5174f94d9767bc8042cb69e6593be00a21"},
                {"y": 158, "x": 216, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=216&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=1bd4de25d8d8c600467c40c984f1edd6b652c8b0"},
                {"y": 235, "x": 320, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=320&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=e7ee2f335ce11a1f461720464fc0878a4d0b200f"},
                {"y": 470, "x": 640, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=640&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=ab6cc54c16fc97d0dd646dc1d3ae4c00cf88695e"},
                {"y": 706, "x": 960, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=960&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=d0616a5a7f24e1a7f68a6d48b8ffba8bea54d9d3"},
                {"y": 794, "x": 1080, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=1080&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=006e88894394def39f3266b1093983d359499b20"}
            ],
            "s": {"y": 1704, "x": 2316, "u": "https://preview.redd.it/v8dmkhn60vxa1.png?width=2316&amp;format=png&amp;auto=webp&amp;v=enabled&amp;s=9d3bdbc8f85be08c514383cc1e2cf23908b97a0c"},
            "id": "v8dmkhn60vxa1"
        },
        "g7doc1f60vxa1": {"status": "valid", "e": "Image", "m": "image/png", "o": [{"y": 1704, "x": 2316, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=1080&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=97ec2c25ad77cab3d52d1d23fc02449d95ce4688"}], "p": [{"y": 79, "x": 108, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=108&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=095c27ba2cce8e7b75e27938663fd92d98b38219"}, {"y": 158, "x": 216, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=216&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=0de8370efdb994126661d55fc0d78ec23d147e52"}, {"y": 235, "x": 320, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=320&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=a6f43055b7fa697f95c21e0141d69260e1036fa2"}, {"y": 470, "x": 640, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=640&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=c31d4637ecfd19ee996944e4e9827348e5ea7631"}, {"y": 706, "x": 960, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=960&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=a9e55f6281e803abfe229f5018f8290143d9c81b"}, {"y": 794, "x": 1080, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=1080&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=a77bba8befd72a2b295c3d6185b1ec21dabc72dc"}], "s": {"y": 1704, "x": 2316, "u": "https://preview.redd.it/g7doc1f60vxa1.png?width=2316&amp;format=png&amp;auto=webp&amp;v=enabled&amp;s=75ef71e1495ae28efd1c4338d5749f4657ee5f80"}, "id": "g7doc1f60vxa1"}
    },
    "name": "t3_137vxcf",
    "quarantine": False,
    "link_flair_text_color": "light",
    "upvote_ratio": 0.99,
    "author_flair_background_color": None,
    "ups": 116,
    "domain": "reddit.com",
    "media_embed": {},
    "thumbnail_width": 140,
    "author_flair_template_id": None,
    "is_original_content": None,
    "user_reports": [],
    "secure_media": None,
    "is_reddit_media_domain": False,
    "is_meta": False,
    "category": None,
    "secure_media_embed": {},
    "gallery_data": {"items": [
        {"media_id": "g7doc1f60vxa1", "id": 271145194},
        {"media_id": "v8dmkhn60vxa1", "id": 271145195}
    ]},
    "link_flair_text": "Public",
    "can_mod_post": False,
    "score": 116,
    "approved_by": None,
    "is_created_from_ads_ui": False,
    "author_premium": False,
    "thumbnail": "https://b.thumbs.redditmedia.com/ueiRLa-nnD_sWBFDR4djkZlFKhac76nT-3e7nSYNCYA.jpg",
    "edited": False,
    "author_flair_css_class": None,
    "author_flair_richtext": [],
    "gildings": {},
    "content_categories": None,
    "is_self": False,
    "subreddit_type": "public",
    "created": 1683225534.0,
    "link_flair_type": "text",
    "wls": None,
    "removed_by_category": None,
    "banned_by": None,
    "author_flair_type": "text",
    "total_awards_received": 0,
    "allow_live_comments": False,
    "selftext_html": None,
    "likes": None,
    "suggested_sort": "new",
    "banned_at_utc": None,
    "url_overridden_by_dest": "https://www.reddit.com/gallery/137vxcf",
    "view_count": None,
    "archived": False, "no_follow": False,
    "is_crosspostable": False,
    "pinned": False,
    "over_18": True,
    "all_awardings": [],
    "awarders": [],
    "media_only": False,
    "link_flair_template_id": "ed2b41fc-5483-11ed-9196-86187a33d490",
    "can_gild": True,
    "spoiler": False,
    "locked": False,
    "author_flair_text": None,
    "treatment_tags": [],
    "visited": False,
    "removed_by": None,
    "mod_note": None,
    "distinguished": None,
    "subreddit_id": "t5_2clyih",
    "author_is_blocked": False,
    "mod_reason_by": None,
    "num_reports": None,
    "removal_reason": None,
    "link_flair_background_color": "#af1249",
    "id": "137vxcf",
    "is_robot_indexable": True,
    "report_reasons": None,
    "author": "Klutzy_Arachnid9172", 
    "discussion_type": None, 
    "num_comments": 3, 
    "send_replies": True, 
    "whitelist_status": None, 
    # "contest_mode": False, "mod_reports": [], "author_patreon_flair": False, "author_flair_text_color": None, "permalink": "/r/HentaiBondageTales/comments/137vxcf/a_weekend_at_the_beach/", "parent_whitelist_status": None, "stickied": False, "url": "https://www.reddit.com/gallery/137vxcf", "subreddit_subscribers": 34164, "created_utc": 1683225534.0, "num_crossposts": 0, "media": None, "is_video": False}}, {"kind": "t3", "data": {"approved_at_utc": None, "subreddit": "HentaiBondageTales", "selftext": "", "author_fullname": "t2_3plx6xsp", "saved": False, "mod_reason_title": None, "gilded": 0, "clicked": False, "title": "Princess Zelda, the Ponygirl (Commissioned Caption)", "link_flair_richtext": [], "subreddit_name_prefixed": "r/HentaiBondageTales", "hidden": False, "pwls": None, "link_flair_css_class": "", "downs": 0, "thumbnail_height": 140, "top_awarded_type": None, "hide_score": False, "name": "t3_137muwk", "quarantine": False, "link_flair_text_color": "dark", "upvote_ratio": 0.99, "author_flair_background_color": None, "ups": 295, "total_awards_received": 0, "media_embed": {}, "thumbnail_width": 140, "author_flair_template_id": None, "is_original_content": False, "user_reports": [], "secure_media": None, "is_reddit_media_domain": True, "is_meta": False, "category": None, "secure_media_embed": {}, "link_flair_text": "Bitchsuit / petplay", "can_mod_post": False, "score": 295, "approved_by": None, "is_created_from_ads_ui": False, "author_premium": False, "thumbnail": "https://b.thumbs.redditmedia.com/z6RDLYVz_XqKqyYDzaf9ZLT0RMVMAtA-0-mbjQQEoQQ.jpg", "edited": False, "author_flair_css_class": None, "author_flair_richtext": [], "gildings": {}, "post_hint": "image", "content_categories": None, "is_self": False, "subreddit_type": "public", "created": 1683210668.0, "link_flair_type": "text", "wls": None, "removed_by_category": None, "banned_by": None, "author_flair_type": "text", "domain": "i.redd.it", "allow_live_comments": False, "selftext_html": None, "likes": None, "suggested_sort": "new", "banned_at_utc": None, "url_overridden_by_dest": "https://i.redd.it/evjas11i9vxa1.jpg", "view_count": None, "archived": False, "no_follow": False, "is_crosspostable": True, "pinned": False, "over_18": True, "preview": {"images": [{"source": {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?auto=webp&amp;v=enabled&amp;s=a534ad96f243afa6049a4b28e03467de0351c757", "width": 4077, "height": 4096}, "resolutions": [{"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=108&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=1f6095c6d4b4ac0b3e43a4e2800570380d1cff26", "width": 108, "height": 108}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=216&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=8bb7f0e27cb117b8c756e128c07137157bfce41d", "width": 216, "height": 217}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=320&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=9c58513a390be9c7f488a436082114e387b3ed39", "width": 320, "height": 321}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=640&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=aeea87dc907c08456967f9e39ca43724955e238e", "width": 640, "height": 642}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=960&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=31fd991f2544ff4bf559f85dc0702c142921528d", "width": 960, "height": 964}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=1080&amp;crop=smart&amp;auto=webp&amp;v=enabled&amp;s=5bd8784068bea204fcddb18c5928214df242220e", "width": 1080, "height": 1085}], "variants": {"obfuscated": {"source": {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=36e3fa76b2b1a63a693d5b27821bd58e56ee34cf", "width": 4077, "height": 4096}, "resolutions": [{"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=108&amp;crop=smart&amp;blur=10&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=6a7e49a6586e3ef3373d06e828de1a1a767abb8a", "width": 108, "height": 108}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=216&amp;crop=smart&amp;blur=21&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=5da3388a170ba068d776f37553b2f641baa42e9b", "width": 216, "height": 217}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=320&amp;crop=smart&amp;blur=32&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=755f78d5f92b9fc1cb8fced987002b2bc174575f", "width": 320, "height": 321}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=640&amp;crop=smart&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=3c63418b83c24caf1812db8de7f665339a4c4cdb", "width": 640, "height": 642}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=960&amp;crop=smart&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=a0030092a43a04e790f7cc12d294959dee2f43c0", "width": 960, "height": 964}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=1080&amp;crop=smart&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=59e50afbd5e8d09bdbb7110f120e11c9fe1a0e00", "width": 1080, "height": 1085}]}, "nsfw": {"source": {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=36e3fa76b2b1a63a693d5b27821bd58e56ee34cf", "width": 4077, "height": 4096}, "resolutions": [{"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=108&amp;crop=smart&amp;blur=10&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=6a7e49a6586e3ef3373d06e828de1a1a767abb8a", "width": 108, "height": 108}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=216&amp;crop=smart&amp;blur=21&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=5da3388a170ba068d776f37553b2f641baa42e9b", "width": 216, "height": 217}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=320&amp;crop=smart&amp;blur=32&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=755f78d5f92b9fc1cb8fced987002b2bc174575f", "width": 320, "height": 321}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=640&amp;crop=smart&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=3c63418b83c24caf1812db8de7f665339a4c4cdb", "width": 640, "height": 642}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=960&amp;crop=smart&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=a0030092a43a04e790f7cc12d294959dee2f43c0", "width": 960, "height": 964}, {"url": "https://preview.redd.it/evjas11i9vxa1.jpg?width=1080&amp;crop=smart&amp;blur=40&amp;format=pjpg&amp;auto=webp&amp;v=enabled&amp;s=59e50afbd5e8d09bdbb7110f120e11c9fe1a0e00", "width": 1080, "height": 1085}]}
}



@dataclass
class Post:
    json: dict

    @property
    def subreddit(self) -> str:
        return self.json.get("subreddit")

    @property
    def title(self) -> str:
        return self.json.get("title")

    @property
    def id(self):
        return self.json.get("name")

    @property
    def flair(self) -> str:
        return self.json.get("link_flair_text")

    @property
    def date(self) -> datetime:
        return datetime.fromtimestamp(int(self.json.get("created", 0)))

    @property
    def artist(self) -> str:
        return self.json.get("author")

    def __str__(self):
        return f"{self.date} r/{self.subreddit} - {self.title} ({self.flair}) by u/{self.artist}"