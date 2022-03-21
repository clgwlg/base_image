# -*- coding: utf-8 -*-
import cv2
import numpy as np
from numpy.core import generic

from typing import Tuple, Union, overload

from .constant import Place
from .coordinate import Rect, Size


class _Image(object):
    _data: Union[np.ndarray, cv2.cuda.GpuMat, cv2.Mat, cv2.UMat]
    _read_mode: int
    _place: int
    def __init__(self, data: Union[str, bytes, np.ndarray, cv2.cuda.GpuMat, cv2.Mat, cv2.UMat],
                 read_mode: int = cv2.IMREAD_COLOR, dtype: generic = np.uint8, place: int = Place.Mat, clone: bool = True): ...

    def write(self, data: Union[str, bytes, np.ndarray, cv2.cuda.GpuMat, cv2.Mat, cv2.UMat],
              read_mode: int = None, dtype=None, place=None, clone=True) -> None: ...

    @classmethod
    def _create_mat(cls, data: Union[np.ndarray, cv2.Mat], shape: Union[tuple, list]) -> cv2.Mat: ...

    def dtype_convert(self, dtype) -> None: ...

    def place_convert(self, place) -> None: ...

    @property
    def shape(self) -> Tuple[int, int, int]: ...

    @property
    def size(self) -> Tuple[int, int]: ...

    @property
    def channels(self) -> int: ...

    @property
    def dtype(self): ...

    @property
    def place(self) -> int: ...

    @property
    def data(self) -> Union[np.ndarray, cv2.cuda.GpuMat, cv2.Mat, cv2.UMat]: ...


class Image(_Image):
    def clone(self) -> Image:
        pass

    def _clone_with_params(self, data, **kwargs) -> Image: ...

    @overload
    def resize(self, w: int, h: int) -> Image: ...

    @overload
    def resize(self, size: Size) -> Image: ...

    def cvtColor(self, code: int) -> Image: ...

    def crop(self, rect: Rect) -> Image: ...

    def threshold(self, thresh: int = 0, maxval: int = 255, code=cv2.THRESH_OTSU) -> Image: ...

    def rectangle(self, rect: Rect, color: Tuple[int, int, int] = (0, 255, 0), thickness: int = 1, lineType=cv2.LINE_8) -> None: ...

    def gaussianBlur(self, size: Tuple[int, int] = (0, 0), sigma: Union[int, float] = 1.5, borderType: int = cv2.BORDER_DEFAULT) -> Image: ...

    def bitwise_not(self, mask=None) -> Image: ...

    def imshow(self, title: str = None, flag: int = cv2.WINDOW_KEEPRATIO) -> None: ...

    def imwrite(self, fileName: str) -> None: ...

    def split(self) -> Tuple[Union[np.ndarray, cv2.cuda.GpuMat, cv2.UMat], ...]: ...
