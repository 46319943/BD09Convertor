# BD09Convertor
BD09 coordinates conversion tool for Python.
- From BD09LL to BD09MC
- From BD09MC to BD09LL

Python版本的BD09坐标转换工具
- 从BD09LL转为BD09MC
- 从BD09MC转为BD09LL

# Install
```
pip install bd09convertor
```

Or specify the `index-url` if your mirror hasn't cache the package.
```
pip install bd09convertor -i https://pypi.org/simple
```

# Usage
```
from bd09convertor import convertMC2LL, convertLL2MC

convertMC2LL(12943772.884424742, 4832666.423350099) 
# return (116.27462499999993, 39.96162707324356)

convertLL2MC(116.274625, 39.961627) 
# return (12943772.884424742, 4832666.423350099)
```

# Reference
BD09 is a CRS(Coordinate Reference System) encrypted by Baidu based on GCJ09 CRS.

BD09LL represents longitude and latitude.
BD09MC represents coordinate with meter based unit like Web Mercator projection.

BD09：为百度坐标系，在GCJ02坐标系基础上再次加密。其中bd09ll表示百度经纬度坐标，bd09mc表示百度墨卡托米制坐标。

Ref: `https://lbsyun.baidu.com/index.php?title=coordinate`