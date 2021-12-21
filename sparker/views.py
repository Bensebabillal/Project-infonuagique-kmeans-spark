from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sparker.serializers import ItemSerializer


@api_view(['POST'])
def snippet_list(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            # read pickled model via pipeline api
            from pyspark.ml.pipeline import PipelineModel
            persistedModel = PipelineModel.load('../myModel')
            model2 = KMeansModel.load(model_path)
            model2.hasSummary
            model.clusterCenters()[0] == model2.clusterCenters()[0]
            array([ True,  True], dtype=bool)
            model.clusterCenters()[1] == model2.clusterCenters()[1]
            array([ True,  True], dtype=bool)
            model.transform(df).take(1) == model2.transform(df).take(1)


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
