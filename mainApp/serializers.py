from rest_framework import serializers

from mainApp.models import category, customCategory, product


class getProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class getSubCategoriesSerializer(serializers.ModelSerializer):
    # subs = getProductsSerializer(many=True)
    class Meta:
        model = customCategory
        fields = ('id','title','image','category','subs')

class getCustomCategoriesSerializer(serializers.ModelSerializer):
    subs = getSubCategoriesSerializer(many=True)

    class Meta:
        model = category
        fields = ('id',
                  'title',
                  'description',
                  'image',
                  'type',
                  'subs')



# class getStCategoriesSerializer(serializers.ModelSerializer):
#     subs = getSubCategoriesSerializer(many=True)
#
#     class Meta:
#         model = category
#         fields = ('id',
#                   'title',
#                   'description',
#                   'image',
#                   'type',
#                   'subs')
