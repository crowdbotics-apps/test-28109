from .. import models
from Functions.DynamicSer import DynamicSerializer
from Functions.MyViews import ItemView, ItemsView

MyModel = models.AlertsRules


class ModelSer(DynamicSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class Views(ItemsView):
    def post(self,*args,**kwargs):
        """
        # Quick examples:
            - to say if new patient added then notify doctors and providers
            `{
            "model": "user",
            "field":"group",
            "field_value":"patient",
            'groups':['doctors','providers']
            }`

            - if user oxgyen level__lt=80 then notify doctors and providers
            `{
            "model": "statistics",
            "filter":"column__name=oxgyen_level",
            "field":"field_value",
            "field_value":"__lt=80",
            'groups':['doctors','providers']
            }`
        """
        return super().post(*args,**kwargs)
    queryset = MyModel.objects.all()
    serializer_class = ModelSer


class View(ItemView):
    MyModel = MyModel
    queryset = MyModel.objects.all()
    serializer_class = ModelSer
