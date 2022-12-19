import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class MonitorConfig(AppConfig):
    name = 'monitor'
    MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeModel.joblib")
    #MODEL_FILE=r'H:\vaibhav\PycharmProjects\ML\ML-Django\mainapp\ml\model\DecisionTreeModel.joblib'
    #MODEL_FILE = r'H:\\vaibhav\\PycharmProjects\\ML\\ML-Django\\mainapp\\ml\\model\\DecisionTreeModel.joblib'
    model = joblib.load(MODEL_FILE)
