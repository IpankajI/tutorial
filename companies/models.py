from django.db import models
import collections
import hashlib
# from jsonfield import JSONField
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Stock(models.Model):
	ticker=models.CharField(max_length=10)
	openn=models.FloatField()
	close=models.FloatField()
	volume=models.IntegerField()
	# config=JSONField(_('configuration'),
 #                       default=dict,
 #                       help_text=_('configuration in NetJSON DeviceConfiguration format'),
 #                       load_kwargs={'object_pairs_hook': collections.OrderedDict},
 #                       dump_kwargs={'indent': 4})
	def __str__(self):
		return self.ticker