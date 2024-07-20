class EnablePartialUpdateMixin:
    """
    Enable Partial Update for Adding Workouts to Exercise
    Override partial kwargs in UpdateModelMixin Class
    """

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)
