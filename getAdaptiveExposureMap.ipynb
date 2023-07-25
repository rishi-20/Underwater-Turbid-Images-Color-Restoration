{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cdb743b6",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'GuidedFilter'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [1], line 4\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mcv2\u001b[39;00m\n\u001b[1;32m----> 4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mGuidedFilter\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m GuidedFilter\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mguidedfilter_He\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m guided_filter_he\n\u001b[0;32m      7\u001b[0m np\u001b[38;5;241m.\u001b[39mseterr(over\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mignore\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'GuidedFilter'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "\n",
    "from GuidedFilter import GuidedFilter\n",
    "from guidedfilter_He import guided_filter_he\n",
    "\n",
    "np.seterr(over='ignore')\n",
    "np.seterr(invalid ='ignore')\n",
    "np.seterr(all ='ignore')\n",
    "\n",
    "\n",
    "#\n",
    "#  def AdaptiveExposureMap(img,sceneRadiance,Lambda,blockSize):\n",
    "#     img = np.float32(img)\n",
    "#     sceneRadiance = np.float32(sceneRadiance)\n",
    "#\n",
    "#     x = sceneRadiance * img + Lambda * (img **2 )\n",
    "#     y = sceneRadiance ** 2 + Lambda *  (img ** 2)\n",
    "#     S_x  = x / y\n",
    "#\n",
    "#     return S_x\n",
    "\n",
    "\n",
    "\n",
    "def AdaptiveExposureMap(img, sceneRadiance, Lambda, blockSize):\n",
    "\n",
    "    minValue = 10 ** -2\n",
    "    img = np.uint8(img)\n",
    "    sceneRadiance = np.uint8(sceneRadiance)\n",
    "\n",
    "    YjCrCb = cv2.cvtColor(sceneRadiance, cv2.COLOR_BGR2YCrCb)\n",
    "    YiCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)\n",
    "    normYjCrCb = (YjCrCb - YjCrCb.min()) / (YjCrCb.max() - YjCrCb.min())\n",
    "    normYiCrCb = (YiCrCb - YiCrCb.min()) / (YiCrCb.max() - YiCrCb.min())\n",
    "    Yi = normYiCrCb[:, :, 0]\n",
    "    Yj = normYjCrCb[:, :, 0]\n",
    "    Yi = np.clip(Yi, minValue,1)\n",
    "    Yj = np.clip(Yj, minValue,1)\n",
    "\n",
    "    # print('np.min(Yi)',np.min(Yi))\n",
    "    # print('np.max(Yi)',np.max(Yi))\n",
    "    # print('np.min(Yj)',np.min(Yj))\n",
    "    # print('np.max(Yj)',np.max(Yj))\n",
    "    # Yi = YiCrCb[:, :, 0]\n",
    "    # Yj = YjCrCb[:, :, 0]\n",
    "    S = (Yj * Yi + 0.3 * Yi ** 2) / (Yj ** 2 + 0.3 * Yi ** 2)\n",
    "\n",
    "    # print('S',S)\n",
    "\n",
    "    gimfiltR = 50  \n",
    "    eps = 10 ** -3  \n",
    "\n",
    "    # refinedS = guided_filter_he(YiCrCb, S, gimfiltR, eps)\n",
    "\n",
    "    guided_filter = GuidedFilter(YiCrCb, gimfiltR, eps)\n",
    "    # guided_filter = GuidedFilter(normYiCrCb, gimfiltR, eps)\n",
    "\n",
    "    refinedS = guided_filter.filter(S)\n",
    "\n",
    "    # print('guided_filter_he(YiCrCb, S, gimfiltR, eps)', refinedS)\n",
    "    # S = np.clip(S, 0, 1)\n",
    "\n",
    "    # cv2.imwrite('OutputImages_D/' + 'SSSSS' + '_GBdehazingRCorrectionStretching.jpg', np.uint8(S * 255))\n",
    "\n",
    "    S_three = np.zeros(img.shape)\n",
    "    S_three[:, :, 0] = S_three[:, :, 1] = S_three[:, :, 2] = refinedS\n",
    "\n",
    "    return S_three"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95a14627",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
