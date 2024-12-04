

class ModelValidationMixin:
    """
    A mixin for calling model validation in the serializer.
    """

    def validate(self, attrs):
        instance = self.Meta.model(**attrs)

        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return attrs