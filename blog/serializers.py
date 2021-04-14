from rest_framework import serializers
from .models import Post, PostFile

"""def isBase64(s):
    import base64
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False"""

"""class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isBase64(data):
            if isinstance(data, six.string_types):
                if 'data:' in data and ';base64,' in data:
                    header, data = data.split(';base64,')

                try:
                    decoded_file = base64.b64decode(data)
                except TypeError:
                    self.fail('invalid_image')

                file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
                file_extension = self.get_file_extension(file_name, decoded_file)
                complete_file_name = "%s.%s" % (file_name, file_extension, )
                data = ContentFile(decoded_file, name=complete_file_name)

            return super(Base64ImageField, self).to_internal_value(data)
        else:            
            return None

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
"""

class PostSerializer(serializers.ModelSerializer):            
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'published')
        model = Post
    

class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'file')
        model = PostFile
