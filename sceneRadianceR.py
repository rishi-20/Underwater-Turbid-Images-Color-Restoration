{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38407d20",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def  sceneradiance(img, sceneRadiance_GB):\n",
    "    img = np.float32(img)\n",
    "    R_original = img[:, :, 2]\n",
    "    sceneRadiance_GB = np.float32(sceneRadiance_GB)\n",
    "\n",
    "    print('***********************************************************')\n",
    "    avgRr = 1.5 - (np.mean(sceneRadiance_GB[:,:,0])/255 +np.mean(sceneRadiance_GB[:,:,1])/255)\n",
    "    parameterR  =   avgRr  / ((np.mean(R_original))/255)\n",
    "\n",
    "    print('parameterR',parameterR)\n",
    "    sceneRadianceR = R_original * parameterR\n",
    "    sceneRadianceR = (sceneRadianceR - sceneRadianceR.min()) / (sceneRadianceR.max() - sceneRadianceR.min())\n",
    "    sceneRadianceR = sceneRadianceR * 255\n",
    "\n",
    "    sceneRadianceR = np.clip(sceneRadianceR, 0, 255)\n",
    "    sceneRadiance_GB[:, :, 2] = sceneRadianceR\n",
    "    sceneRadiance_GB = np.uint8(sceneRadiance_GB)\n",
    "    return  sceneRadiance_GB\n"
   ]
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
