import uuid
import json
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MonetaryPenalty(models.Model):
    monetary_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity_id = models.CharField(max_length=255, blank=True, null=True)
    premiseId = models.CharField(max_length=255, blank=True, null=True)
    startDate = models.CharField(max_length=255, blank=True, null=True)
    endDate = models.CharField(max_length=255, blank=True, null=True)
    penaltyAuthority = models.CharField(max_length=255, blank=True, null=True)
    penaltyCurrency = models.CharField(max_length=255, blank=True, null=True)
    penaltyAmount = models.CharField(max_length=255, blank=True, null=True)
    penaltyCase = models.CharField(max_length=255, blank=True, null=True)
    penaltyAppeal = models.CharField(max_length=255, blank=True, null=True)
    penaltyAppealReason = models.CharField(max_length=255, blank=True, null=True)
    penaltyAppealFile = models.CharField(max_length=255, null=True, blank=True)
    settlementAuthority = models.CharField(max_length=255, blank=True, null=True)
    settlementCurrency = models.CharField(max_length=255, blank=True, null=True)
    settlementAmount = models.CharField(max_length=255, blank=True, null=True)
    settlementCase = models.CharField(max_length=255, blank=True, null=True)
    settlementAppeal = models.CharField(max_length=255, blank=True, null=True)
    settlementAppealReason = models.CharField(max_length=255, blank=True, null=True)
    settlementAppealFile = models.CharField(max_length=255, null=True, blank=True)
    compoundFeeAuthority = models.CharField(max_length=255, blank=True, null=True)
    compoundFeeCurrency = models.CharField(max_length=255, blank=True, null=True)
    compoundFeeAmount = models.CharField(max_length=255, blank=True, null=True)
    compoundFeeCase = models.CharField(max_length=255, blank=True, null=True)
    compoundFeeAppeal = models.CharField(max_length=255, blank=True, null=True)
    compoundAppealReason = models.CharField(max_length=255, blank=True, null=True)
    compoundAppealFile = models.CharField(max_length=255, null=True, blank=True)
    createdBy = models.CharField(max_length=255, blank=True, null=True)
    createdOn = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'MONETARY_PENALTY'


class FileMetadata(models.Model):
    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    data = models.BinaryField()
    file_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'FILE'

@receiver(post_save, sender=MonetaryPenalty)
def create_file_metadata(sender, instance, created, **kwargs):
    if created:
        # Generate a unique UUID for the name
        unique_id = str(uuid.uuid4())

       # Serialize the MonetaryPenalty object's fields into JSON format and encode it as bytes
       

        monetary_penalty_data = {
            "entity_id": instance.entity_id,
            "premiseId": instance.premiseId,
            "startDate": instance.startDate,
            "endDate": instance.endDate,
            "penaltyAuthority": instance.penaltyAuthority,
            "penaltyCurrency": instance.penaltyCurrency,
            "penaltyAmount": instance.penaltyAmount,
            "penaltyCase": instance.penaltyCase,
            "penaltyAppeal": instance.penaltyAppeal,
            "penaltyAppealReason": instance.penaltyAppealReason,
            "penaltyAppealFile": instance.penaltyAppealFile,
            "settlementAuthority": instance.settlementAuthority,
            "settlementCurrency": instance.settlementCurrency,
            "settlementAmount": instance.settlementAmount,
            "settlementCase": instance.settlementCase,
            "settlementAppeal": instance.settlementAppeal,
            "settlementAppealReason": instance.settlementAppealReason,
            "settlementAppealFile": instance.settlementAppealFile,
            "compoundFeeAuthority": instance.compoundFeeAuthority,
            "compoundFeeCurrency": instance.compoundFeeCurrency,
            "compoundFeeAmount": instance.compoundFeeAmount,
            "compoundFeeCase": instance.compoundFeeCase,
            "compoundFeeAppeal": instance.compoundFeeAppeal,
            "compoundAppealReason": instance.compoundAppealReason,
            "compoundAppealFile": instance.compoundAppealFile,
            "createdBy": instance.createdBy,
            "createdOn": instance.createdOn,
            # Add more fields as needed
        }

        # Serialize the dictionary to JSON format
        data_json = json.dumps(monetary_penalty_data).encode()


        # Create the FileMetadata record with the serialized data
        FileMetadata.objects.create(
            name=unique_id,
            data=data_json,
            file_type='json',
            description=f'{unique_id} JSON file is created with MonetaryPenalty data',
        )
