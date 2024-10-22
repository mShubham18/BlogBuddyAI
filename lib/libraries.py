import sys
from src.BlogBuddyAI import logger
from src.BlogBuddyAI.exception import CustomException
import streamlit as st
import google.generativeai as genai
import os
#from openai import openai
import requests
import json
import time