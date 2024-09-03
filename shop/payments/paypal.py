import paypalrestsdk
import logging


logging.basicConfig(level=logging.INFO)


paypalrestsdk.configure({
    "mode": "live", 
    "client_id": "AbX7EGIGP9bHV1TeduRJg6fLr2i1pltX-ezUcGssZ1HXuGvY2V-9p9t959BOoCs2DdcGCqK3SlfCO3qu",
    "client_secret": "ED_cZDu_3hTcfIUJcOnnUpTamnQkciWjh0F6VjdqfdEihUKguRGghi4lybYPfi39MCYrBOv930Jf9sD4"
})