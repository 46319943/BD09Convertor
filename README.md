# BD09Convertor
BD09/WGS84 coordinates conversion tool for Python.
- From BD09LL to BD09MC
- From BD09MC to BD09LL
- From BD09LL to WGS84
- From WGS84 to BD09LL
- From BD09MC to WGS84
- From WGS84 to BD09MC

Python版本的BD09/WGS84坐标转换工具
- 从BD09LL转为BD09MC
- 从BD09MC转为BD09LL
- 从BD09LL转为WGS84
- 从WGS84转为BD09LL
- 从BD09MC转为WGS84
- 从WGS84转为BD09MC

# Install
```
pip install bd09convertor
```

Or specify the `index-url` if your mirror hasn't cached the package.
```
pip install bd09convertor -i https://pypi.org/simple
```

# Usage
```
from bd09convertor import (
    convertMC2LL,
    convertLL2MC,
    convertBD09LL2WGS84,
    convertWGS842BD09LL,
    convertBD09MC2WGS84,
    convertWGS842BD09MC,
)

# BD09MC <-> BD09LL
convertMC2LL(12943772.884424742, 4832666.423350099)
# return (116.27462499999993, 39.96162707324356)

convertLL2MC(116.274625, 39.961627)
# return (12943772.884424742, 4832666.423350099)

# BD09LL <-> WGS84
convertBD09LL2WGS84(116.28705235117383, 39.969206291127605)
# return (116.27461816438877, 39.96162060897989)

convertWGS842BD09LL(116.274625, 39.961627)
# return (116.28705235117383, 39.969206291127605)

# BD09MC <-> WGS84
convertBD09MC2WGS84(12943772.884424742, 4832666.423350099)
# return (116.26218811167767, 39.95412076177775)

convertWGS842BD09MC(116.274625, 39.961627)
# return (12945156.305881673, 4833762.890529349)
```

# Reference
BD09 is a CRS (Coordinate Reference System) encrypted by Baidu based on GCJ02 CRS.

BD09LL represents longitude and latitude.
BD09MC represents coordinate with meter based unit like Web Mercator projection.

BD09：为百度坐标系，在GCJ02坐标系基础上再次加密。其中bd09ll表示百度经纬度坐标，bd09mc表示百度墨卡托米制坐标。

Ref: `https://lbsyun.baidu.com/index.php?title=coordinate`
