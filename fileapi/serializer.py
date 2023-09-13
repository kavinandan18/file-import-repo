from rest_framework import serializers
from .models import MonetaryPenalty, FileMetadata
from django.http import HttpResponse  
class MonetaryPenaltySerializer(serializers.ModelSerializer):
    EntityId = serializers.CharField(source='entity_id', required=False)
    PremiseId = serializers.CharField(source='premiseId', required=False)
    StartDate = serializers.CharField(source='startDate', required=False)
    EndDate = serializers.CharField(source='endDate', required=False)
    PenaltyAuthority = serializers.CharField(source='penaltyAuthority', required=False)
    PenaltyCurrency = serializers.CharField(source='penaltyCurrency', required=False)
    PenaltyAmount = serializers.CharField(source='penaltyAmount', required=False)
    PenaltyCase = serializers.CharField(source='penaltyCase', required=False)
    PenaltyAppeal = serializers.CharField(source='penaltyAppeal', required=False)
    PenaltyAppealReason = serializers.CharField(source='penaltyAppealReason', required=False)
    PenaltyAppealFile = serializers.CharField(source='penaltyAppealFile', required=False)
    SettlementAuthority = serializers.CharField(source='settlementAuthority', required=False)
    SettlementCurrency = serializers.CharField(source='settlementCurrency', required=False)
    SettlementAmount = serializers.CharField(source='settlementAmount', required=False)
    SettlementCase = serializers.CharField(source='settlementCase', required=False)
    SettlementAppeal = serializers.CharField(source='settlementAppeal', required=False)
    SettlementAppealReason = serializers.CharField(source='settlementAppealReason', required=False)
    SettlementAppealFile = serializers.CharField(source='settlementAppealFile', required=False, allow_blank=True)
    CompoundFeeAuthority = serializers.CharField(source='compoundFeeAuthority', required=False)
    CompoundFeeCurrency = serializers.CharField(source='compoundFeeCurrency', required=False)
    CompoundFeeAmount = serializers.CharField(source='compoundFeeAmount', required=False)
    CompoundFeeCase = serializers.CharField(source='compoundFeeCase', required=False)
    CompoundFeeAppeal = serializers.CharField(source='compoundFeeAppeal', required=False)
    CompoundAppealReason = serializers.CharField(source='compoundAppealReason', required=False)
    CompoundAppealFile = serializers.CharField(source='compoundAppealFile', required=False)
    CreatedBy = serializers.CharField(source='createdBy', required=False)
    CreatedOn = serializers.CharField(source='createdOn', required=False)

    class Meta:
        model = MonetaryPenalty
        fields = '__all__'
     
import base64
import json

class FileMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileMetadata
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context.get('request')
        if request and 'file_id' in request.query_params:
            # Check if 'file_id' is in query parameters
            file_id = request.query_params['file_id']
            if instance.file_id == file_id:
                try:
                    # Decode the binary 'data' field and parse it as JSON
                    data_str = instance.data.decode('utf-8')
                    data_list = json.loads(data_str)

                    # Include the decoded data as a list in the response
                    response_data = {
                        'file_id': str(instance.file_id),
                        'name': instance.name,
                        'data': data_list,
                        'file_type': instance.file_type,
                        'description': instance.description,
                    }
                    return response_data
                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    return super().to_representation(instance)
        # Default behavior, return regular serialization
        return super().to_representation(instance)








