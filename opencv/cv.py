# This file was created automatically by SWIG 1.3.30.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.


import _cv
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class CvRNG_Wrapper(_object):
    """Proxy of C++ CvRNG_Wrapper class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvRNG_Wrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvRNG_Wrapper, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, CvRNG val) -> CvRNG_Wrapper"""
        this = _cv.new_CvRNG_Wrapper(*args)
        try: self.this.append(this)
        except: self.this = this
    def ptr(*args):
        """ptr(self) -> CvRNG"""
        return _cv.CvRNG_Wrapper_ptr(*args)

    def ref(*args):
        """ref(self) -> CvRNG"""
        return _cv.CvRNG_Wrapper_ref(*args)

    def __eq__(*args):
        """__eq__(self, CvRNG_Wrapper x) -> bool"""
        return _cv.CvRNG_Wrapper___eq__(*args)

    def __ne__(*args):
        """__ne__(self, CvRNG_Wrapper x) -> bool"""
        return _cv.CvRNG_Wrapper___ne__(*args)

    __swig_destroy__ = _cv.delete_CvRNG_Wrapper
    __del__ = lambda self : None;
CvRNG_Wrapper_swigregister = _cv.CvRNG_Wrapper_swigregister
CvRNG_Wrapper_swigregister(CvRNG_Wrapper)

class CvSubdiv2DEdge_Wrapper(_object):
    """Proxy of C++ CvSubdiv2DEdge_Wrapper class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSubdiv2DEdge_Wrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSubdiv2DEdge_Wrapper, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, CvSubdiv2DEdge val) -> CvSubdiv2DEdge_Wrapper"""
        this = _cv.new_CvSubdiv2DEdge_Wrapper(*args)
        try: self.this.append(this)
        except: self.this = this
    def ptr(*args):
        """ptr(self) -> CvSubdiv2DEdge"""
        return _cv.CvSubdiv2DEdge_Wrapper_ptr(*args)

    def ref(*args):
        """ref(self) -> CvSubdiv2DEdge"""
        return _cv.CvSubdiv2DEdge_Wrapper_ref(*args)

    def __eq__(*args):
        """__eq__(self, CvSubdiv2DEdge_Wrapper x) -> bool"""
        return _cv.CvSubdiv2DEdge_Wrapper___eq__(*args)

    def __ne__(*args):
        """__ne__(self, CvSubdiv2DEdge_Wrapper x) -> bool"""
        return _cv.CvSubdiv2DEdge_Wrapper___ne__(*args)

    __swig_destroy__ = _cv.delete_CvSubdiv2DEdge_Wrapper
    __del__ = lambda self : None;
CvSubdiv2DEdge_Wrapper_swigregister = _cv.CvSubdiv2DEdge_Wrapper_swigregister
CvSubdiv2DEdge_Wrapper_swigregister(CvSubdiv2DEdge_Wrapper)

def cvCalcHist(*args):
	return cvCalcArrHist(*args)


def cvSegmentMotion(*args):
  """
    cvSegmentMotion(CvArr mhi, CvArr seg_mask, CvMemStorage storage, double timestamp, 
        double seg_thresh) -> CvSeq_CvConnectedComp
    """
  return _cv.cvSegmentMotion(*args)
def cvHoughCircles(*args):
	seq = cvHoughCirclesUntyped( *args )
	return CvSeq_float_3.cast(seq)

def cvPyrSegmentation(*args):
	seq = cvPyrSegmentationUntyped( *args )
	return CvSeq_CvConnectedComp.cast(seq)

def cvApproxChains(*args):
	seq = cvApproxChainsUntyped( *args )
	return CvSeq_CvPoint.cast(seq)

def cvContourFromContourTree(*args):
	seq = cvContourFromContourTreeUntyped( *args )
	return CvSeq_CvPoint.cast(seq)

def cvConvexityDefects(*args):
	seq = cvConvexityDefectsUntyped( *args )
	return CvSeq_CvConvexityDefect.cast(seq)

def cvFindContours( *args ):
	count, seq = cvFindContoursUntyped( *args )
	return count, CvSeq_CvPoint.cast(seq)

def cvHoughLines2( *args ):
	seq = cvHoughLinesUntyped( *args )
	type = CV_SEQ_ELTYPE(seq) 
	if type == CV_32SC4:
		return CvSeq_CvPoint_2.cast(seq)
	return CvSeq_float_2.cast(seq)


def cvReleaseImage(*args):
  """cvReleaseImage(PyObject obj)"""
  return _cv.cvReleaseImage(*args)

def cvReleaseMat(*args):
  """cvReleaseMat(PyObject obj)"""
  return _cv.cvReleaseMat(*args)

def cvReleaseStructuringElement(*args):
  """cvReleaseStructuringElement(PyObject obj)"""
  return _cv.cvReleaseStructuringElement(*args)

def cvReleaseConDensation(*args):
  """cvReleaseConDensation(PyObject obj)"""
  return _cv.cvReleaseConDensation(*args)

def cvReleaseKalman(*args):
  """cvReleaseKalman(PyObject obj)"""
  return _cv.cvReleaseKalman(*args)

def cvReleaseHist(*args):
  """cvReleaseHist(PyObject obj)"""
  return _cv.cvReleaseHist(*args)

def cvReleaseHaarClassifierCascade(*args):
  """cvReleaseHaarClassifierCascade(PyObject obj)"""
  return _cv.cvReleaseHaarClassifierCascade(*args)

def cvReleasePOSITObject(*args):
  """cvReleasePOSITObject(PyObject obj)"""
  return _cv.cvReleasePOSITObject(*args)

def cvReleaseImageHeader(*args):
  """cvReleaseImageHeader(PyObject obj)"""
  return _cv.cvReleaseImageHeader(*args)

def cvReleaseMatND(*args):
  """cvReleaseMatND(PyObject obj)"""
  return _cv.cvReleaseMatND(*args)

def cvReleaseSparseMat(*args):
  """cvReleaseSparseMat(PyObject obj)"""
  return _cv.cvReleaseSparseMat(*args)

def cvReleaseMemStorage(*args):
  """cvReleaseMemStorage(PyObject obj)"""
  return _cv.cvReleaseMemStorage(*args)

def cvReleaseGraphScanner(*args):
  """cvReleaseGraphScanner(PyObject obj)"""
  return _cv.cvReleaseGraphScanner(*args)

def cvReleaseFileStorage(*args):
  """cvReleaseFileStorage(PyObject obj)"""
  return _cv.cvReleaseFileStorage(*args)

def cvRelease(*args):
  """cvRelease(PyObject obj)"""
  return _cv.cvRelease(*args)

def cvReleaseCapture(*args):
  """cvReleaseCapture(PyObject obj)"""
  return _cv.cvReleaseCapture(*args)

def cvReleaseVideoWriter(*args):
  """cvReleaseVideoWriter(PyObject obj)"""
  return _cv.cvReleaseVideoWriter(*args)

def cvFree(*args):
  """cvFree(void ptr)"""
  return _cv.cvFree(*args)

def CV_READ_CHAIN_POINT(*args):
  """CV_READ_CHAIN_POINT(CvPoint _pt, CvChainPtReader reader)"""
  return _cv.CV_READ_CHAIN_POINT(*args)

def CV_MAT_ELEM_PTR(*args):
  """CV_MAT_ELEM_PTR(CvMat mat, int row, int col) -> void"""
  return _cv.CV_MAT_ELEM_PTR(*args)

def CV_MAT_ELEM_PTR_FAST(*args):
  """CV_MAT_ELEM_PTR_FAST(CvMat mat, int row, int col, int pix_size) -> void"""
  return _cv.CV_MAT_ELEM_PTR_FAST(*args)

def CV_NODE_VAL(*args):
  """CV_NODE_VAL(CvSparseMat mat, CvSparseNode node) -> void"""
  return _cv.CV_NODE_VAL(*args)

def CV_NODE_IDX(*args):
  """CV_NODE_IDX(CvSparseMat mat, CvSparseNode node) -> int"""
  return _cv.CV_NODE_IDX(*args)

def CV_SUBDIV2D_NEXT_EDGE(*args):
  """CV_SUBDIV2D_NEXT_EDGE(CvSubdiv2DEdge edge) -> CvQuadEdge2D"""
  return _cv.CV_SUBDIV2D_NEXT_EDGE(*args)

def CV_SWAP(*args):
  """CV_SWAP(int a, int b, int t)"""
  return _cv.CV_SWAP(*args)

def CV_IMIN(*args):
  """CV_IMIN(int a, int b) -> int"""
  return _cv.CV_IMIN(*args)

def CV_IMAX(*args):
  """CV_IMAX(int a, int b) -> int"""
  return _cv.CV_IMAX(*args)

def CV_IABS(*args):
  """CV_IABS(int a) -> int"""
  return _cv.CV_IABS(*args)

def CV_CMP(*args):
  """CV_CMP(int a, int b)"""
  return _cv.CV_CMP(*args)

def CV_SIGN(*args):
  """CV_SIGN(int a)"""
  return _cv.CV_SIGN(*args)

def cvInvSqrt(*args):
  """cvInvSqrt(double value)"""
  return _cv.cvInvSqrt(*args)

def cvSqrt(*args):
  """cvSqrt(double value)"""
  return _cv.cvSqrt(*args)

def CV_IS_IMAGE_HDR(*args):
  """CV_IS_IMAGE_HDR(CvArr img) -> int"""
  return _cv.CV_IS_IMAGE_HDR(*args)

def CV_IS_IMAGE(*args):
  """CV_IS_IMAGE(CvArr img) -> int"""
  return _cv.CV_IS_IMAGE(*args)

def CV_MAKETYPE(*args):
  """CV_MAKETYPE(int depth, int cn) -> int"""
  return _cv.CV_MAKETYPE(*args)

def CV_8UC(*args):
  """CV_8UC(int n) -> int"""
  return _cv.CV_8UC(*args)

def CV_8SC(*args):
  """CV_8SC(int n) -> int"""
  return _cv.CV_8SC(*args)

def CV_16UC(*args):
  """CV_16UC(int n) -> int"""
  return _cv.CV_16UC(*args)

def CV_16SC(*args):
  """CV_16SC(int n) -> int"""
  return _cv.CV_16SC(*args)

def CV_32SC(*args):
  """CV_32SC(int n) -> int"""
  return _cv.CV_32SC(*args)

def CV_32FC(*args):
  """CV_32FC(int n) -> int"""
  return _cv.CV_32FC(*args)

def CV_64FC(*args):
  """CV_64FC(int n) -> int"""
  return _cv.CV_64FC(*args)

def CV_MAT_CN(*args):
  """CV_MAT_CN(int flags) -> int"""
  return _cv.CV_MAT_CN(*args)

def CV_MAT_DEPTH(*args):
  """CV_MAT_DEPTH(int flags) -> int"""
  return _cv.CV_MAT_DEPTH(*args)

def CV_MAT_TYPE(*args):
  """CV_MAT_TYPE(int flags) -> int"""
  return _cv.CV_MAT_TYPE(*args)

def CV_IS_MAT_CONT(*args):
  """CV_IS_MAT_CONT(int flags) -> int"""
  return _cv.CV_IS_MAT_CONT(*args)

def CV_IS_TEMP_MAT(*args):
  """CV_IS_TEMP_MAT(int flags) -> int"""
  return _cv.CV_IS_TEMP_MAT(*args)

def CV_IS_MAT_HDR(*args):
  """CV_IS_MAT_HDR(CvMat mat) -> int"""
  return _cv.CV_IS_MAT_HDR(*args)

def CV_IS_MAT(*args):
  """CV_IS_MAT(CvMat mat) -> int"""
  return _cv.CV_IS_MAT(*args)

def CV_IS_MASK_ARR(*args):
  """CV_IS_MASK_ARR(CvMat mat) -> int"""
  return _cv.CV_IS_MASK_ARR(*args)

def CV_ARE_TYPES_EQ(*args):
  """CV_ARE_TYPES_EQ(CvMat mat1, CvMat mat2) -> int"""
  return _cv.CV_ARE_TYPES_EQ(*args)

def CV_ARE_CNS_EQ(*args):
  """CV_ARE_CNS_EQ(CvMat mat1, CvMat mat2) -> int"""
  return _cv.CV_ARE_CNS_EQ(*args)

def CV_ARE_DEPTHS_EQ(*args):
  """CV_ARE_DEPTHS_EQ(CvMat mat1, CvMat mat2) -> int"""
  return _cv.CV_ARE_DEPTHS_EQ(*args)

def CV_ARE_SIZES_EQ(*args):
  """CV_ARE_SIZES_EQ(CvMat mat1, CvMat mat2) -> int"""
  return _cv.CV_ARE_SIZES_EQ(*args)

def CV_IS_MAT_CONST(*args):
  """CV_IS_MAT_CONST(CvMat mat) -> int"""
  return _cv.CV_IS_MAT_CONST(*args)

def CV_ELEM_SIZE1(*args):
  """CV_ELEM_SIZE1(int type) -> int"""
  return _cv.CV_ELEM_SIZE1(*args)

def CV_ELEM_SIZE(*args):
  """CV_ELEM_SIZE(int type) -> int"""
  return _cv.CV_ELEM_SIZE(*args)

def CV_IS_MATND_HDR(*args):
  """CV_IS_MATND_HDR(CvMat mat) -> int"""
  return _cv.CV_IS_MATND_HDR(*args)

def CV_IS_MATND(*args):
  """CV_IS_MATND(CvMat mat) -> int"""
  return _cv.CV_IS_MATND(*args)

def CV_IS_SPARSE_MAT_HDR(*args):
  """CV_IS_SPARSE_MAT_HDR(CvMat mat) -> int"""
  return _cv.CV_IS_SPARSE_MAT_HDR(*args)

def CV_IS_SPARSE_MAT(*args):
  """CV_IS_SPARSE_MAT(CvMat mat) -> int"""
  return _cv.CV_IS_SPARSE_MAT(*args)

def CV_IS_HIST(*args):
  """CV_IS_HIST(CvHistogram hist) -> int"""
  return _cv.CV_IS_HIST(*args)

def CV_IS_UNIFORM_HIST(*args):
  """CV_IS_UNIFORM_HIST(CvHistogram hist) -> int"""
  return _cv.CV_IS_UNIFORM_HIST(*args)

def CV_IS_SPARSE_HIST(*args):
  """CV_IS_SPARSE_HIST(CvHistogram hist) -> int"""
  return _cv.CV_IS_SPARSE_HIST(*args)

def CV_HIST_HAS_RANGES(*args):
  """CV_HIST_HAS_RANGES(CvHistogram hist) -> int"""
  return _cv.CV_HIST_HAS_RANGES(*args)

def CV_IS_STORAGE(*args):
  """CV_IS_STORAGE(CvMemStorage storage) -> int"""
  return _cv.CV_IS_STORAGE(*args)

def CV_IS_SET_ELEM(*args):
  """CV_IS_SET_ELEM(void ptr) -> int"""
  return _cv.CV_IS_SET_ELEM(*args)

def CV_IS_SEQ(*args):
  """CV_IS_SEQ(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ(*args)

def CV_IS_SET(*args):
  """CV_IS_SET(CvSet set) -> int"""
  return _cv.CV_IS_SET(*args)

def CV_SEQ_ELTYPE(*args):
  """CV_SEQ_ELTYPE(CvSeq seq) -> int"""
  return _cv.CV_SEQ_ELTYPE(*args)

def CV_SEQ_KIND(*args):
  """CV_SEQ_KIND(CvSeq seq) -> int"""
  return _cv.CV_SEQ_KIND(*args)

def CV_IS_SEQ_INDEX(*args):
  """CV_IS_SEQ_INDEX(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_INDEX(*args)

def CV_IS_SEQ_CURVE(*args):
  """CV_IS_SEQ_CURVE(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_CURVE(*args)

def CV_IS_SEQ_CLOSED(*args):
  """CV_IS_SEQ_CLOSED(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_CLOSED(*args)

def CV_IS_SEQ_CONVEX(*args):
  """CV_IS_SEQ_CONVEX(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_CONVEX(*args)

def CV_IS_SEQ_HOLE(*args):
  """CV_IS_SEQ_HOLE(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_HOLE(*args)

def CV_IS_SEQ_SIMPLE(*args):
  """CV_IS_SEQ_SIMPLE(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_SIMPLE(*args)

def CV_IS_SEQ_POINT_SET(*args):
  """CV_IS_SEQ_POINT_SET(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_POINT_SET(*args)

def CV_IS_SEQ_POINT_SUBSET(*args):
  """CV_IS_SEQ_POINT_SUBSET(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_POINT_SUBSET(*args)

def CV_IS_SEQ_POLYLINE(*args):
  """CV_IS_SEQ_POLYLINE(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_POLYLINE(*args)

def CV_IS_SEQ_POLYGON(*args):
  """CV_IS_SEQ_POLYGON(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_POLYGON(*args)

def CV_IS_SEQ_CHAIN(*args):
  """CV_IS_SEQ_CHAIN(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_CHAIN(*args)

def CV_IS_SEQ_CONTOUR(*args):
  """CV_IS_SEQ_CONTOUR(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_CONTOUR(*args)

def CV_IS_SEQ_CHAIN_CONTOUR(*args):
  """CV_IS_SEQ_CHAIN_CONTOUR(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_CHAIN_CONTOUR(*args)

def CV_IS_SEQ_POLYGON_TREE(*args):
  """CV_IS_SEQ_POLYGON_TREE(CvSeq seq) -> int"""
  return _cv.CV_IS_SEQ_POLYGON_TREE(*args)

def CV_IS_GRAPH(*args):
  """CV_IS_GRAPH(CvSeq seq) -> int"""
  return _cv.CV_IS_GRAPH(*args)

def CV_IS_GRAPH_ORIENTED(*args):
  """CV_IS_GRAPH_ORIENTED(CvSeq seq) -> int"""
  return _cv.CV_IS_GRAPH_ORIENTED(*args)

def CV_IS_SUBDIV2D(*args):
  """CV_IS_SUBDIV2D(CvSeq seq) -> int"""
  return _cv.CV_IS_SUBDIV2D(*args)

def CV_WRITE_SEQ_ELEM_VAR(*args):
  """CV_WRITE_SEQ_ELEM_VAR(void elem_ptr, CvSeqWriter writer)"""
  return _cv.CV_WRITE_SEQ_ELEM_VAR(*args)

def CV_WRITE_SEQ_ELEM(*args):
  """CV_WRITE_SEQ_ELEM(CvPoint elem, CvSeqWriter writer)"""
  return _cv.CV_WRITE_SEQ_ELEM(*args)

def CV_NEXT_SEQ_ELEM(*args):
  """CV_NEXT_SEQ_ELEM(int elem_size, CvSeqReader reader)"""
  return _cv.CV_NEXT_SEQ_ELEM(*args)

def CV_PREV_SEQ_ELEM(*args):
  """CV_PREV_SEQ_ELEM(int elem_size, CvSeqReader reader)"""
  return _cv.CV_PREV_SEQ_ELEM(*args)

def CV_READ_SEQ_ELEM(*args):
  """CV_READ_SEQ_ELEM(CvPoint elem, CvSeqReader reader)"""
  return _cv.CV_READ_SEQ_ELEM(*args)

def CV_REV_READ_SEQ_ELEM(*args):
  """CV_REV_READ_SEQ_ELEM(CvPoint elem, CvSeqReader reader)"""
  return _cv.CV_REV_READ_SEQ_ELEM(*args)

def CV_CURRENT_POINT(*args):
  """CV_CURRENT_POINT(CvSeqReader reader) -> CvPoint"""
  return _cv.CV_CURRENT_POINT(*args)

def CV_PREV_POINT(*args):
  """CV_PREV_POINT(CvSeqReader reader) -> CvPoint"""
  return _cv.CV_PREV_POINT(*args)

def CV_READ_EDGE(*args):
  """CV_READ_EDGE(CvPoint pt1, CvPoint pt2, CvSeqReader reader)"""
  return _cv.CV_READ_EDGE(*args)

def CV_NEXT_GRAPH_EDGE(*args):
  """CV_NEXT_GRAPH_EDGE(CvGraphEdge edge, CvGraphVtx vertex) -> CvGraphEdge"""
  return _cv.CV_NEXT_GRAPH_EDGE(*args)

def CV_NODE_TYPE(*args):
  """CV_NODE_TYPE(int flags) -> int"""
  return _cv.CV_NODE_TYPE(*args)

def CV_NODE_IS_INT(*args):
  """CV_NODE_IS_INT(int flags) -> int"""
  return _cv.CV_NODE_IS_INT(*args)

def CV_NODE_IS_REAL(*args):
  """CV_NODE_IS_REAL(int flags) -> int"""
  return _cv.CV_NODE_IS_REAL(*args)

def CV_NODE_IS_STRING(*args):
  """CV_NODE_IS_STRING(int flags) -> int"""
  return _cv.CV_NODE_IS_STRING(*args)

def CV_NODE_IS_SEQ(*args):
  """CV_NODE_IS_SEQ(int flags) -> int"""
  return _cv.CV_NODE_IS_SEQ(*args)

def CV_NODE_IS_MAP(*args):
  """CV_NODE_IS_MAP(int flags) -> int"""
  return _cv.CV_NODE_IS_MAP(*args)

def CV_NODE_IS_COLLECTION(*args):
  """CV_NODE_IS_COLLECTION(int flags) -> int"""
  return _cv.CV_NODE_IS_COLLECTION(*args)

def CV_NODE_IS_FLOW(*args):
  """CV_NODE_IS_FLOW(int flags) -> int"""
  return _cv.CV_NODE_IS_FLOW(*args)

def CV_NODE_IS_EMPTY(*args):
  """CV_NODE_IS_EMPTY(int flags) -> int"""
  return _cv.CV_NODE_IS_EMPTY(*args)

def CV_NODE_IS_USER(*args):
  """CV_NODE_IS_USER(int flags) -> int"""
  return _cv.CV_NODE_IS_USER(*args)

def CV_NODE_HAS_NAME(*args):
  """CV_NODE_HAS_NAME(int flags) -> int"""
  return _cv.CV_NODE_HAS_NAME(*args)

def CV_NODE_SEQ_IS_SIMPLE(*args):
  """CV_NODE_SEQ_IS_SIMPLE(CvSeq seq) -> int"""
  return _cv.CV_NODE_SEQ_IS_SIMPLE(*args)

def cvReshapeND(*args):
  """
    cvReshapeND(CvArr arr, CvMat header, int new_cn, int new_dims, 
        int new_sizes)
    """
  return _cv.cvReshapeND(*args)

def cvConvert(*args):
  """cvConvert(CvArr src, CvArr dst)"""
  return _cv.cvConvert(*args)

def cvAXPY(*args):
  """cvAXPY(CvArr A, double real_scalar, CvArr B, CvArr C)"""
  return _cv.cvAXPY(*args)

def cvAbs(*args):
  """cvAbs(CvArr src, CvArr dst)"""
  return _cv.cvAbs(*args)

def cvMatMulAdd(*args):
  """cvMatMulAdd(CvArr src1, CvArr src2, CvArr src3, CvArr dst)"""
  return _cv.cvMatMulAdd(*args)

def cvMatMul(*args):
  """cvMatMul(CvArr src1, CvArr src2, CvArr dst)"""
  return _cv.cvMatMul(*args)

def cvGetGraphVtx(*args):
  """cvGetGraphVtx(CvGraph graph, int idx)"""
  return _cv.cvGetGraphVtx(*args)

def cvGraphVtxIdx(*args):
  """cvGraphVtxIdx(CvGraph graph, CvGraphVtx vtx) -> int"""
  return _cv.cvGraphVtxIdx(*args)

def cvGraphEdgeIdx(*args):
  """cvGraphEdgeIdx(CvGraph graph, CvGraphEdge edge) -> int"""
  return _cv.cvGraphEdgeIdx(*args)

def cvGraphGetVtxCount(*args):
  """cvGraphGetVtxCount(CvGraph graph) -> int"""
  return _cv.cvGraphGetVtxCount(*args)

def cvGraphGetEdgeCount(*args):
  """cvGraphGetEdgeCount(CvGraph graph) -> int"""
  return _cv.cvGraphGetEdgeCount(*args)

def CV_IS_GRAPH_VERTEX_VISITED(*args):
  """CV_IS_GRAPH_VERTEX_VISITED(CvGraphVtx vtx) -> int"""
  return _cv.CV_IS_GRAPH_VERTEX_VISITED(*args)

def CV_IS_GRAPH_EDGE_VISITED(*args):
  """CV_IS_GRAPH_EDGE_VISITED(CvGraphEdge edge) -> int"""
  return _cv.CV_IS_GRAPH_EDGE_VISITED(*args)

def CV_RGB(*args):
  """CV_RGB(double r, double g, int b) -> CvScalar"""
  return _cv.CV_RGB(*args)

def CV_NEXT_LINE_POINT(*args):
  """CV_NEXT_LINE_POINT(CvLineIterator line_iterator)"""
  return _cv.CV_NEXT_LINE_POINT(*args)

def CV_INIT_3X3_DELTAS(*args):
  """CV_INIT_3X3_DELTAS(double deltas, int step, int nch)"""
  return _cv.CV_INIT_3X3_DELTAS(*args)

def CV_IS_HAAR_CLASSIFIER(*args):
  """CV_IS_HAAR_CLASSIFIER(void haar) -> int"""
  return _cv.CV_IS_HAAR_CLASSIFIER(*args)

def cvCalcBackProject(*args):
  """cvCalcBackProject( image, CvArr dst, CvHistogram hist)"""
  return _cv.cvCalcBackProject(*args)

def cvCalcBackProjectPatch(*args):
  """
    cvCalcBackProjectPatch( image, CvArr dst, CvSize range, CvHistogram hist, 
        int method, double factor)
    """
  return _cv.cvCalcBackProjectPatch(*args)
sizeof_CvContour = _cv.sizeof_CvContour
sizeof_CvPoint = _cv.sizeof_CvPoint
sizeof_CvSeq = _cv.sizeof_CvSeq

def cvCreateImage(*args):
  """cvCreateImage(CvSize size, int depth, int channels) -> CvMat"""
  return _cv.cvCreateImage(*args)

def cvCloneImage(*args):
  """cvCloneImage(CvMat mat) -> CvMat"""
  return _cv.cvCloneImage(*args)
CV_AUTOSTEP = _cv.CV_AUTOSTEP
CV_MAX_ARR = _cv.CV_MAX_ARR
CV_NO_DEPTH_CHECK = _cv.CV_NO_DEPTH_CHECK
CV_NO_CN_CHECK = _cv.CV_NO_CN_CHECK
CV_NO_SIZE_CHECK = _cv.CV_NO_SIZE_CHECK
CV_CMP_EQ = _cv.CV_CMP_EQ
CV_CMP_GT = _cv.CV_CMP_GT
CV_CMP_GE = _cv.CV_CMP_GE
CV_CMP_LT = _cv.CV_CMP_LT
CV_CMP_LE = _cv.CV_CMP_LE
CV_CMP_NE = _cv.CV_CMP_NE
CV_CHECK_RANGE = _cv.CV_CHECK_RANGE
CV_CHECK_QUIET = _cv.CV_CHECK_QUIET
CV_RAND_UNI = _cv.CV_RAND_UNI
CV_RAND_NORMAL = _cv.CV_RAND_NORMAL
CV_GEMM_A_T = _cv.CV_GEMM_A_T
CV_GEMM_B_T = _cv.CV_GEMM_B_T
CV_GEMM_C_T = _cv.CV_GEMM_C_T
CV_SVD_MODIFY_A = _cv.CV_SVD_MODIFY_A
CV_SVD_U_T = _cv.CV_SVD_U_T
CV_SVD_V_T = _cv.CV_SVD_V_T
CV_LU = _cv.CV_LU
CV_SVD = _cv.CV_SVD
CV_SVD_SYM = _cv.CV_SVD_SYM
CV_COVAR_SCRAMBLED = _cv.CV_COVAR_SCRAMBLED
CV_COVAR_NORMAL = _cv.CV_COVAR_NORMAL
CV_COVAR_USE_AVG = _cv.CV_COVAR_USE_AVG
CV_COVAR_SCALE = _cv.CV_COVAR_SCALE
CV_COVAR_ROWS = _cv.CV_COVAR_ROWS
CV_COVAR_COLS = _cv.CV_COVAR_COLS
CV_PCA_DATA_AS_ROW = _cv.CV_PCA_DATA_AS_ROW
CV_PCA_DATA_AS_COL = _cv.CV_PCA_DATA_AS_COL
CV_PCA_USE_AVG = _cv.CV_PCA_USE_AVG
CV_C = _cv.CV_C
CV_L1 = _cv.CV_L1
CV_L2 = _cv.CV_L2
CV_NORM_MASK = _cv.CV_NORM_MASK
CV_RELATIVE = _cv.CV_RELATIVE
CV_DIFF = _cv.CV_DIFF
CV_MINMAX = _cv.CV_MINMAX
CV_DIFF_C = _cv.CV_DIFF_C
CV_DIFF_L1 = _cv.CV_DIFF_L1
CV_DIFF_L2 = _cv.CV_DIFF_L2
CV_RELATIVE_C = _cv.CV_RELATIVE_C
CV_RELATIVE_L1 = _cv.CV_RELATIVE_L1
CV_RELATIVE_L2 = _cv.CV_RELATIVE_L2
CV_REDUCE_SUM = _cv.CV_REDUCE_SUM
CV_REDUCE_AVG = _cv.CV_REDUCE_AVG
CV_REDUCE_MAX = _cv.CV_REDUCE_MAX
CV_REDUCE_MIN = _cv.CV_REDUCE_MIN
CV_DXT_FORWARD = _cv.CV_DXT_FORWARD
CV_DXT_INVERSE = _cv.CV_DXT_INVERSE
CV_DXT_SCALE = _cv.CV_DXT_SCALE
CV_DXT_INV_SCALE = _cv.CV_DXT_INV_SCALE
CV_DXT_INVERSE_SCALE = _cv.CV_DXT_INVERSE_SCALE
CV_DXT_ROWS = _cv.CV_DXT_ROWS
CV_DXT_MUL_CONJ = _cv.CV_DXT_MUL_CONJ
CV_FRONT = _cv.CV_FRONT
CV_BACK = _cv.CV_BACK
CV_GRAPH_VERTEX = _cv.CV_GRAPH_VERTEX
CV_GRAPH_TREE_EDGE = _cv.CV_GRAPH_TREE_EDGE
CV_GRAPH_BACK_EDGE = _cv.CV_GRAPH_BACK_EDGE
CV_GRAPH_FORWARD_EDGE = _cv.CV_GRAPH_FORWARD_EDGE
CV_GRAPH_CROSS_EDGE = _cv.CV_GRAPH_CROSS_EDGE
CV_GRAPH_ANY_EDGE = _cv.CV_GRAPH_ANY_EDGE
CV_GRAPH_NEW_TREE = _cv.CV_GRAPH_NEW_TREE
CV_GRAPH_BACKTRACKING = _cv.CV_GRAPH_BACKTRACKING
CV_GRAPH_OVER = _cv.CV_GRAPH_OVER
CV_GRAPH_ALL_ITEMS = _cv.CV_GRAPH_ALL_ITEMS
CV_GRAPH_ITEM_VISITED_FLAG = _cv.CV_GRAPH_ITEM_VISITED_FLAG
CV_GRAPH_SEARCH_TREE_NODE_FLAG = _cv.CV_GRAPH_SEARCH_TREE_NODE_FLAG
CV_GRAPH_FORWARD_EDGE_FLAG = _cv.CV_GRAPH_FORWARD_EDGE_FLAG
CV_FILLED = _cv.CV_FILLED
CV_AA = _cv.CV_AA
CV_FONT_HERSHEY_SIMPLEX = _cv.CV_FONT_HERSHEY_SIMPLEX
CV_FONT_HERSHEY_PLAIN = _cv.CV_FONT_HERSHEY_PLAIN
CV_FONT_HERSHEY_DUPLEX = _cv.CV_FONT_HERSHEY_DUPLEX
CV_FONT_HERSHEY_COMPLEX = _cv.CV_FONT_HERSHEY_COMPLEX
CV_FONT_HERSHEY_TRIPLEX = _cv.CV_FONT_HERSHEY_TRIPLEX
CV_FONT_HERSHEY_COMPLEX_SMALL = _cv.CV_FONT_HERSHEY_COMPLEX_SMALL
CV_FONT_HERSHEY_SCRIPT_SIMPLEX = _cv.CV_FONT_HERSHEY_SCRIPT_SIMPLEX
CV_FONT_HERSHEY_SCRIPT_COMPLEX = _cv.CV_FONT_HERSHEY_SCRIPT_COMPLEX
CV_FONT_ITALIC = _cv.CV_FONT_ITALIC
CV_FONT_VECTOR0 = _cv.CV_FONT_VECTOR0
CV_ErrModeLeaf = _cv.CV_ErrModeLeaf
CV_ErrModeParent = _cv.CV_ErrModeParent
CV_ErrModeSilent = _cv.CV_ErrModeSilent
CV_MAJOR_VERSION = _cv.CV_MAJOR_VERSION
CV_MINOR_VERSION = _cv.CV_MINOR_VERSION
CV_SUBMINOR_VERSION = _cv.CV_SUBMINOR_VERSION
CV_VERSION = _cv.CV_VERSION
CV_PI = _cv.CV_PI
CV_LOG2 = _cv.CV_LOG2
IPL_DEPTH_SIGN = _cv.IPL_DEPTH_SIGN
IPL_DEPTH_1U = _cv.IPL_DEPTH_1U
IPL_DEPTH_8U = _cv.IPL_DEPTH_8U
IPL_DEPTH_16U = _cv.IPL_DEPTH_16U
IPL_DEPTH_32F = _cv.IPL_DEPTH_32F
IPL_DEPTH_8S = _cv.IPL_DEPTH_8S
IPL_DEPTH_16S = _cv.IPL_DEPTH_16S
IPL_DEPTH_32S = _cv.IPL_DEPTH_32S
IPL_DATA_ORDER_PIXEL = _cv.IPL_DATA_ORDER_PIXEL
IPL_DATA_ORDER_PLANE = _cv.IPL_DATA_ORDER_PLANE
IPL_ORIGIN_TL = _cv.IPL_ORIGIN_TL
IPL_ORIGIN_BL = _cv.IPL_ORIGIN_BL
IPL_ALIGN_4BYTES = _cv.IPL_ALIGN_4BYTES
IPL_ALIGN_8BYTES = _cv.IPL_ALIGN_8BYTES
IPL_ALIGN_16BYTES = _cv.IPL_ALIGN_16BYTES
IPL_ALIGN_32BYTES = _cv.IPL_ALIGN_32BYTES
IPL_ALIGN_DWORD = _cv.IPL_ALIGN_DWORD
IPL_ALIGN_QWORD = _cv.IPL_ALIGN_QWORD
IPL_BORDER_CONSTANT = _cv.IPL_BORDER_CONSTANT
IPL_BORDER_REPLICATE = _cv.IPL_BORDER_REPLICATE
IPL_BORDER_REFLECT = _cv.IPL_BORDER_REFLECT
IPL_BORDER_WRAP = _cv.IPL_BORDER_WRAP
IPL_IMAGE_HEADER = _cv.IPL_IMAGE_HEADER
IPL_IMAGE_DATA = _cv.IPL_IMAGE_DATA
IPL_IMAGE_ROI = _cv.IPL_IMAGE_ROI
IPL_BORDER_REFLECT_101 = _cv.IPL_BORDER_REFLECT_101
CV_TYPE_NAME_IMAGE = _cv.CV_TYPE_NAME_IMAGE
IPL_DEPTH_64F = _cv.IPL_DEPTH_64F
CV_CN_MAX = _cv.CV_CN_MAX
CV_CN_SHIFT = _cv.CV_CN_SHIFT
CV_DEPTH_MAX = _cv.CV_DEPTH_MAX
CV_8U = _cv.CV_8U
CV_8S = _cv.CV_8S
CV_16U = _cv.CV_16U
CV_16S = _cv.CV_16S
CV_32S = _cv.CV_32S
CV_32F = _cv.CV_32F
CV_64F = _cv.CV_64F
CV_USRTYPE1 = _cv.CV_USRTYPE1
CV_8UC1 = _cv.CV_8UC1
CV_8UC2 = _cv.CV_8UC2
CV_8UC3 = _cv.CV_8UC3
CV_8UC4 = _cv.CV_8UC4
CV_8SC1 = _cv.CV_8SC1
CV_8SC2 = _cv.CV_8SC2
CV_8SC3 = _cv.CV_8SC3
CV_8SC4 = _cv.CV_8SC4
CV_16UC1 = _cv.CV_16UC1
CV_16UC2 = _cv.CV_16UC2
CV_16UC3 = _cv.CV_16UC3
CV_16UC4 = _cv.CV_16UC4
CV_16SC1 = _cv.CV_16SC1
CV_16SC2 = _cv.CV_16SC2
CV_16SC3 = _cv.CV_16SC3
CV_16SC4 = _cv.CV_16SC4
CV_32SC1 = _cv.CV_32SC1
CV_32SC2 = _cv.CV_32SC2
CV_32SC3 = _cv.CV_32SC3
CV_32SC4 = _cv.CV_32SC4
CV_32FC1 = _cv.CV_32FC1
CV_32FC2 = _cv.CV_32FC2
CV_32FC3 = _cv.CV_32FC3
CV_32FC4 = _cv.CV_32FC4
CV_64FC1 = _cv.CV_64FC1
CV_64FC2 = _cv.CV_64FC2
CV_64FC3 = _cv.CV_64FC3
CV_64FC4 = _cv.CV_64FC4
CV_AUTO_STEP = _cv.CV_AUTO_STEP
CV_MAT_CN_MASK = _cv.CV_MAT_CN_MASK
CV_MAT_DEPTH_MASK = _cv.CV_MAT_DEPTH_MASK
CV_MAT_TYPE_MASK = _cv.CV_MAT_TYPE_MASK
CV_MAT_CONT_FLAG_SHIFT = _cv.CV_MAT_CONT_FLAG_SHIFT
CV_MAT_CONT_FLAG = _cv.CV_MAT_CONT_FLAG
CV_MAT_TEMP_FLAG_SHIFT = _cv.CV_MAT_TEMP_FLAG_SHIFT
CV_MAT_TEMP_FLAG = _cv.CV_MAT_TEMP_FLAG
CV_MAGIC_MASK = _cv.CV_MAGIC_MASK
CV_MAT_MAGIC_VAL = _cv.CV_MAT_MAGIC_VAL
CV_TYPE_NAME_MAT = _cv.CV_TYPE_NAME_MAT
CV_MATND_MAGIC_VAL = _cv.CV_MATND_MAGIC_VAL
CV_TYPE_NAME_MATND = _cv.CV_TYPE_NAME_MATND
CV_MAX_DIM = _cv.CV_MAX_DIM
CV_MAX_DIM_HEAP = _cv.CV_MAX_DIM_HEAP
CV_SPARSE_MAT_MAGIC_VAL = _cv.CV_SPARSE_MAT_MAGIC_VAL
CV_TYPE_NAME_SPARSE_MAT = _cv.CV_TYPE_NAME_SPARSE_MAT
CV_HIST_MAGIC_VAL = _cv.CV_HIST_MAGIC_VAL
CV_HIST_UNIFORM_FLAG = _cv.CV_HIST_UNIFORM_FLAG
CV_HIST_RANGES_FLAG = _cv.CV_HIST_RANGES_FLAG
CV_HIST_ARRAY = _cv.CV_HIST_ARRAY
CV_HIST_SPARSE = _cv.CV_HIST_SPARSE
CV_HIST_TREE = _cv.CV_HIST_TREE
CV_HIST_UNIFORM = _cv.CV_HIST_UNIFORM
CV_TERMCRIT_ITER = _cv.CV_TERMCRIT_ITER
CV_TERMCRIT_NUMBER = _cv.CV_TERMCRIT_NUMBER
CV_TERMCRIT_EPS = _cv.CV_TERMCRIT_EPS
CV_WHOLE_SEQ_END_INDEX = _cv.CV_WHOLE_SEQ_END_INDEX
CV_STORAGE_MAGIC_VAL = _cv.CV_STORAGE_MAGIC_VAL
CV_TYPE_NAME_SEQ = _cv.CV_TYPE_NAME_SEQ
CV_TYPE_NAME_SEQ_TREE = _cv.CV_TYPE_NAME_SEQ_TREE
CV_SET_ELEM_IDX_MASK = _cv.CV_SET_ELEM_IDX_MASK
CV_TYPE_NAME_GRAPH = _cv.CV_TYPE_NAME_GRAPH
CV_SEQ_MAGIC_VAL = _cv.CV_SEQ_MAGIC_VAL
CV_SET_MAGIC_VAL = _cv.CV_SET_MAGIC_VAL
CV_SEQ_ELTYPE_BITS = _cv.CV_SEQ_ELTYPE_BITS
CV_SEQ_ELTYPE_MASK = _cv.CV_SEQ_ELTYPE_MASK
CV_SEQ_ELTYPE_POINT = _cv.CV_SEQ_ELTYPE_POINT
CV_SEQ_ELTYPE_CODE = _cv.CV_SEQ_ELTYPE_CODE
CV_SEQ_ELTYPE_GENERIC = _cv.CV_SEQ_ELTYPE_GENERIC
CV_SEQ_ELTYPE_PTR = _cv.CV_SEQ_ELTYPE_PTR
CV_SEQ_ELTYPE_PPOINT = _cv.CV_SEQ_ELTYPE_PPOINT
CV_SEQ_ELTYPE_INDEX = _cv.CV_SEQ_ELTYPE_INDEX
CV_SEQ_ELTYPE_GRAPH_EDGE = _cv.CV_SEQ_ELTYPE_GRAPH_EDGE
CV_SEQ_ELTYPE_GRAPH_VERTEX = _cv.CV_SEQ_ELTYPE_GRAPH_VERTEX
CV_SEQ_ELTYPE_TRIAN_ATR = _cv.CV_SEQ_ELTYPE_TRIAN_ATR
CV_SEQ_ELTYPE_CONNECTED_COMP = _cv.CV_SEQ_ELTYPE_CONNECTED_COMP
CV_SEQ_ELTYPE_POINT3D = _cv.CV_SEQ_ELTYPE_POINT3D
CV_SEQ_KIND_BITS = _cv.CV_SEQ_KIND_BITS
CV_SEQ_KIND_MASK = _cv.CV_SEQ_KIND_MASK
CV_SEQ_KIND_GENERIC = _cv.CV_SEQ_KIND_GENERIC
CV_SEQ_KIND_CURVE = _cv.CV_SEQ_KIND_CURVE
CV_SEQ_KIND_BIN_TREE = _cv.CV_SEQ_KIND_BIN_TREE
CV_SEQ_KIND_GRAPH = _cv.CV_SEQ_KIND_GRAPH
CV_SEQ_KIND_SUBDIV2D = _cv.CV_SEQ_KIND_SUBDIV2D
CV_SEQ_FLAG_SHIFT = _cv.CV_SEQ_FLAG_SHIFT
CV_SEQ_FLAG_CLOSED = _cv.CV_SEQ_FLAG_CLOSED
CV_SEQ_FLAG_SIMPLE = _cv.CV_SEQ_FLAG_SIMPLE
CV_SEQ_FLAG_CONVEX = _cv.CV_SEQ_FLAG_CONVEX
CV_SEQ_FLAG_HOLE = _cv.CV_SEQ_FLAG_HOLE
CV_GRAPH_FLAG_ORIENTED = _cv.CV_GRAPH_FLAG_ORIENTED
CV_GRAPH = _cv.CV_GRAPH
CV_ORIENTED_GRAPH = _cv.CV_ORIENTED_GRAPH
CV_SEQ_POINT_SET = _cv.CV_SEQ_POINT_SET
CV_SEQ_POINT3D_SET = _cv.CV_SEQ_POINT3D_SET
CV_SEQ_POLYLINE = _cv.CV_SEQ_POLYLINE
CV_SEQ_POLYGON = _cv.CV_SEQ_POLYGON
CV_SEQ_CONTOUR = _cv.CV_SEQ_CONTOUR
CV_SEQ_SIMPLE_POLYGON = _cv.CV_SEQ_SIMPLE_POLYGON
CV_SEQ_CHAIN = _cv.CV_SEQ_CHAIN
CV_SEQ_CHAIN_CONTOUR = _cv.CV_SEQ_CHAIN_CONTOUR
CV_SEQ_POLYGON_TREE = _cv.CV_SEQ_POLYGON_TREE
CV_SEQ_CONNECTED_COMP = _cv.CV_SEQ_CONNECTED_COMP
CV_SEQ_INDEX = _cv.CV_SEQ_INDEX
CV_STORAGE_READ = _cv.CV_STORAGE_READ
CV_STORAGE_WRITE = _cv.CV_STORAGE_WRITE
CV_STORAGE_WRITE_TEXT = _cv.CV_STORAGE_WRITE_TEXT
CV_STORAGE_WRITE_BINARY = _cv.CV_STORAGE_WRITE_BINARY
CV_STORAGE_APPEND = _cv.CV_STORAGE_APPEND
CV_NODE_NONE = _cv.CV_NODE_NONE
CV_NODE_INT = _cv.CV_NODE_INT
CV_NODE_INTEGER = _cv.CV_NODE_INTEGER
CV_NODE_REAL = _cv.CV_NODE_REAL
CV_NODE_FLOAT = _cv.CV_NODE_FLOAT
CV_NODE_STR = _cv.CV_NODE_STR
CV_NODE_STRING = _cv.CV_NODE_STRING
CV_NODE_REF = _cv.CV_NODE_REF
CV_NODE_SEQ = _cv.CV_NODE_SEQ
CV_NODE_MAP = _cv.CV_NODE_MAP
CV_NODE_TYPE_MASK = _cv.CV_NODE_TYPE_MASK
CV_NODE_FLOW = _cv.CV_NODE_FLOW
CV_NODE_USER = _cv.CV_NODE_USER
CV_NODE_EMPTY = _cv.CV_NODE_EMPTY
CV_NODE_NAMED = _cv.CV_NODE_NAMED
CV_NODE_SEQ_SIMPLE = _cv.CV_NODE_SEQ_SIMPLE
CV_StsOk = _cv.CV_StsOk
CV_StsBackTrace = _cv.CV_StsBackTrace
CV_StsError = _cv.CV_StsError
CV_StsInternal = _cv.CV_StsInternal
CV_StsNoMem = _cv.CV_StsNoMem
CV_StsBadArg = _cv.CV_StsBadArg
CV_StsBadFunc = _cv.CV_StsBadFunc
CV_StsNoConv = _cv.CV_StsNoConv
CV_StsAutoTrace = _cv.CV_StsAutoTrace
CV_HeaderIsNull = _cv.CV_HeaderIsNull
CV_BadImageSize = _cv.CV_BadImageSize
CV_BadOffset = _cv.CV_BadOffset
CV_BadDataPtr = _cv.CV_BadDataPtr
CV_BadStep = _cv.CV_BadStep
CV_BadModelOrChSeq = _cv.CV_BadModelOrChSeq
CV_BadNumChannels = _cv.CV_BadNumChannels
CV_BadNumChannel1U = _cv.CV_BadNumChannel1U
CV_BadDepth = _cv.CV_BadDepth
CV_BadAlphaChannel = _cv.CV_BadAlphaChannel
CV_BadOrder = _cv.CV_BadOrder
CV_BadOrigin = _cv.CV_BadOrigin
CV_BadAlign = _cv.CV_BadAlign
CV_BadCallBack = _cv.CV_BadCallBack
CV_BadTileSize = _cv.CV_BadTileSize
CV_BadCOI = _cv.CV_BadCOI
CV_BadROISize = _cv.CV_BadROISize
CV_MaskIsTiled = _cv.CV_MaskIsTiled
CV_StsNullPtr = _cv.CV_StsNullPtr
CV_StsVecLengthErr = _cv.CV_StsVecLengthErr
CV_StsFilterStructContentErr = _cv.CV_StsFilterStructContentErr
CV_StsKernelStructContentErr = _cv.CV_StsKernelStructContentErr
CV_StsFilterOffsetErr = _cv.CV_StsFilterOffsetErr
CV_StsBadSize = _cv.CV_StsBadSize
CV_StsDivByZero = _cv.CV_StsDivByZero
CV_StsInplaceNotSupported = _cv.CV_StsInplaceNotSupported
CV_StsObjectNotFound = _cv.CV_StsObjectNotFound
CV_StsUnmatchedFormats = _cv.CV_StsUnmatchedFormats
CV_StsBadFlag = _cv.CV_StsBadFlag
CV_StsBadPoint = _cv.CV_StsBadPoint
CV_StsBadMask = _cv.CV_StsBadMask
CV_StsUnmatchedSizes = _cv.CV_StsUnmatchedSizes
CV_StsUnsupportedFormat = _cv.CV_StsUnsupportedFormat
CV_StsOutOfRange = _cv.CV_StsOutOfRange
CV_StsParseError = _cv.CV_StsParseError
CV_StsNotImplemented = _cv.CV_StsNotImplemented
CV_StsBadMemBlock = _cv.CV_StsBadMemBlock
CV_BLUR_NO_SCALE = _cv.CV_BLUR_NO_SCALE
CV_BLUR = _cv.CV_BLUR
CV_GAUSSIAN = _cv.CV_GAUSSIAN
CV_MEDIAN = _cv.CV_MEDIAN
CV_BILATERAL = _cv.CV_BILATERAL
CV_INPAINT_NS = _cv.CV_INPAINT_NS
CV_INPAINT_TELEA = _cv.CV_INPAINT_TELEA
CV_SCHARR = _cv.CV_SCHARR
CV_MAX_SOBEL_KSIZE = _cv.CV_MAX_SOBEL_KSIZE
CV_BGR2BGRA = _cv.CV_BGR2BGRA
CV_RGB2RGBA = _cv.CV_RGB2RGBA
CV_BGRA2BGR = _cv.CV_BGRA2BGR
CV_RGBA2RGB = _cv.CV_RGBA2RGB
CV_BGR2RGBA = _cv.CV_BGR2RGBA
CV_RGB2BGRA = _cv.CV_RGB2BGRA
CV_RGBA2BGR = _cv.CV_RGBA2BGR
CV_BGRA2RGB = _cv.CV_BGRA2RGB
CV_BGR2RGB = _cv.CV_BGR2RGB
CV_RGB2BGR = _cv.CV_RGB2BGR
CV_BGRA2RGBA = _cv.CV_BGRA2RGBA
CV_RGBA2BGRA = _cv.CV_RGBA2BGRA
CV_BGR2GRAY = _cv.CV_BGR2GRAY
CV_RGB2GRAY = _cv.CV_RGB2GRAY
CV_GRAY2BGR = _cv.CV_GRAY2BGR
CV_GRAY2RGB = _cv.CV_GRAY2RGB
CV_GRAY2BGRA = _cv.CV_GRAY2BGRA
CV_GRAY2RGBA = _cv.CV_GRAY2RGBA
CV_BGRA2GRAY = _cv.CV_BGRA2GRAY
CV_RGBA2GRAY = _cv.CV_RGBA2GRAY
CV_BGR2BGR565 = _cv.CV_BGR2BGR565
CV_RGB2BGR565 = _cv.CV_RGB2BGR565
CV_BGR5652BGR = _cv.CV_BGR5652BGR
CV_BGR5652RGB = _cv.CV_BGR5652RGB
CV_BGRA2BGR565 = _cv.CV_BGRA2BGR565
CV_RGBA2BGR565 = _cv.CV_RGBA2BGR565
CV_BGR5652BGRA = _cv.CV_BGR5652BGRA
CV_BGR5652RGBA = _cv.CV_BGR5652RGBA
CV_GRAY2BGR565 = _cv.CV_GRAY2BGR565
CV_BGR5652GRAY = _cv.CV_BGR5652GRAY
CV_BGR2BGR555 = _cv.CV_BGR2BGR555
CV_RGB2BGR555 = _cv.CV_RGB2BGR555
CV_BGR5552BGR = _cv.CV_BGR5552BGR
CV_BGR5552RGB = _cv.CV_BGR5552RGB
CV_BGRA2BGR555 = _cv.CV_BGRA2BGR555
CV_RGBA2BGR555 = _cv.CV_RGBA2BGR555
CV_BGR5552BGRA = _cv.CV_BGR5552BGRA
CV_BGR5552RGBA = _cv.CV_BGR5552RGBA
CV_GRAY2BGR555 = _cv.CV_GRAY2BGR555
CV_BGR5552GRAY = _cv.CV_BGR5552GRAY
CV_BGR2XYZ = _cv.CV_BGR2XYZ
CV_RGB2XYZ = _cv.CV_RGB2XYZ
CV_XYZ2BGR = _cv.CV_XYZ2BGR
CV_XYZ2RGB = _cv.CV_XYZ2RGB
CV_BGR2YCrCb = _cv.CV_BGR2YCrCb
CV_RGB2YCrCb = _cv.CV_RGB2YCrCb
CV_YCrCb2BGR = _cv.CV_YCrCb2BGR
CV_YCrCb2RGB = _cv.CV_YCrCb2RGB
CV_BGR2HSV = _cv.CV_BGR2HSV
CV_RGB2HSV = _cv.CV_RGB2HSV
CV_BGR2Lab = _cv.CV_BGR2Lab
CV_RGB2Lab = _cv.CV_RGB2Lab
CV_BayerBG2BGR = _cv.CV_BayerBG2BGR
CV_BayerGB2BGR = _cv.CV_BayerGB2BGR
CV_BayerRG2BGR = _cv.CV_BayerRG2BGR
CV_BayerGR2BGR = _cv.CV_BayerGR2BGR
CV_BayerBG2RGB = _cv.CV_BayerBG2RGB
CV_BayerGB2RGB = _cv.CV_BayerGB2RGB
CV_BayerRG2RGB = _cv.CV_BayerRG2RGB
CV_BayerGR2RGB = _cv.CV_BayerGR2RGB
CV_BGR2Luv = _cv.CV_BGR2Luv
CV_RGB2Luv = _cv.CV_RGB2Luv
CV_BGR2HLS = _cv.CV_BGR2HLS
CV_RGB2HLS = _cv.CV_RGB2HLS
CV_HSV2BGR = _cv.CV_HSV2BGR
CV_HSV2RGB = _cv.CV_HSV2RGB
CV_Lab2BGR = _cv.CV_Lab2BGR
CV_Lab2RGB = _cv.CV_Lab2RGB
CV_Luv2BGR = _cv.CV_Luv2BGR
CV_Luv2RGB = _cv.CV_Luv2RGB
CV_HLS2BGR = _cv.CV_HLS2BGR
CV_HLS2RGB = _cv.CV_HLS2RGB
CV_COLORCVT_MAX = _cv.CV_COLORCVT_MAX
CV_INTER_NN = _cv.CV_INTER_NN
CV_INTER_LINEAR = _cv.CV_INTER_LINEAR
CV_INTER_CUBIC = _cv.CV_INTER_CUBIC
CV_INTER_AREA = _cv.CV_INTER_AREA
CV_WARP_FILL_OUTLIERS = _cv.CV_WARP_FILL_OUTLIERS
CV_WARP_INVERSE_MAP = _cv.CV_WARP_INVERSE_MAP
CV_SHAPE_RECT = _cv.CV_SHAPE_RECT
CV_SHAPE_CROSS = _cv.CV_SHAPE_CROSS
CV_SHAPE_ELLIPSE = _cv.CV_SHAPE_ELLIPSE
CV_SHAPE_CUSTOM = _cv.CV_SHAPE_CUSTOM
CV_MOP_OPEN = _cv.CV_MOP_OPEN
CV_MOP_CLOSE = _cv.CV_MOP_CLOSE
CV_MOP_GRADIENT = _cv.CV_MOP_GRADIENT
CV_MOP_TOPHAT = _cv.CV_MOP_TOPHAT
CV_MOP_BLACKHAT = _cv.CV_MOP_BLACKHAT
CV_TM_SQDIFF = _cv.CV_TM_SQDIFF
CV_TM_SQDIFF_NORMED = _cv.CV_TM_SQDIFF_NORMED
CV_TM_CCORR = _cv.CV_TM_CCORR
CV_TM_CCORR_NORMED = _cv.CV_TM_CCORR_NORMED
CV_TM_CCOEFF = _cv.CV_TM_CCOEFF
CV_TM_CCOEFF_NORMED = _cv.CV_TM_CCOEFF_NORMED
CV_LKFLOW_PYR_A_READY = _cv.CV_LKFLOW_PYR_A_READY
CV_LKFLOW_PYR_B_READY = _cv.CV_LKFLOW_PYR_B_READY
CV_LKFLOW_INITIAL_GUESSES = _cv.CV_LKFLOW_INITIAL_GUESSES
CV_POLY_APPROX_DP = _cv.CV_POLY_APPROX_DP
CV_DOMINANT_IPAN = _cv.CV_DOMINANT_IPAN
CV_CONTOURS_MATCH_I1 = _cv.CV_CONTOURS_MATCH_I1
CV_CONTOURS_MATCH_I2 = _cv.CV_CONTOURS_MATCH_I2
CV_CONTOURS_MATCH_I3 = _cv.CV_CONTOURS_MATCH_I3
CV_CONTOUR_TREES_MATCH_I1 = _cv.CV_CONTOUR_TREES_MATCH_I1
CV_CLOCKWISE = _cv.CV_CLOCKWISE
CV_COUNTER_CLOCKWISE = _cv.CV_COUNTER_CLOCKWISE
CV_COMP_CORREL = _cv.CV_COMP_CORREL
CV_COMP_CHISQR = _cv.CV_COMP_CHISQR
CV_COMP_INTERSECT = _cv.CV_COMP_INTERSECT
CV_COMP_BHATTACHARYYA = _cv.CV_COMP_BHATTACHARYYA
CV_VALUE = _cv.CV_VALUE
CV_ARRAY = _cv.CV_ARRAY
CV_DIST_MASK_3 = _cv.CV_DIST_MASK_3
CV_DIST_MASK_5 = _cv.CV_DIST_MASK_5
CV_DIST_MASK_PRECISE = _cv.CV_DIST_MASK_PRECISE
CV_THRESH_BINARY = _cv.CV_THRESH_BINARY
CV_THRESH_BINARY_INV = _cv.CV_THRESH_BINARY_INV
CV_THRESH_TRUNC = _cv.CV_THRESH_TRUNC
CV_THRESH_TOZERO = _cv.CV_THRESH_TOZERO
CV_THRESH_TOZERO_INV = _cv.CV_THRESH_TOZERO_INV
CV_THRESH_MASK = _cv.CV_THRESH_MASK
CV_THRESH_OTSU = _cv.CV_THRESH_OTSU
CV_ADAPTIVE_THRESH_MEAN_C = _cv.CV_ADAPTIVE_THRESH_MEAN_C
CV_ADAPTIVE_THRESH_GAUSSIAN_C = _cv.CV_ADAPTIVE_THRESH_GAUSSIAN_C
CV_FLOODFILL_FIXED_RANGE = _cv.CV_FLOODFILL_FIXED_RANGE
CV_FLOODFILL_MASK_ONLY = _cv.CV_FLOODFILL_MASK_ONLY
CV_CANNY_L2_GRADIENT = _cv.CV_CANNY_L2_GRADIENT
CV_HOUGH_STANDARD = _cv.CV_HOUGH_STANDARD
CV_HOUGH_PROBABILISTIC = _cv.CV_HOUGH_PROBABILISTIC
CV_HOUGH_MULTI_SCALE = _cv.CV_HOUGH_MULTI_SCALE
CV_HOUGH_GRADIENT = _cv.CV_HOUGH_GRADIENT
CV_HAAR_DO_CANNY_PRUNING = _cv.CV_HAAR_DO_CANNY_PRUNING
CV_HAAR_SCALE_IMAGE = _cv.CV_HAAR_SCALE_IMAGE
CV_CALIB_USE_INTRINSIC_GUESS = _cv.CV_CALIB_USE_INTRINSIC_GUESS
CV_CALIB_FIX_ASPECT_RATIO = _cv.CV_CALIB_FIX_ASPECT_RATIO
CV_CALIB_FIX_PRINCIPAL_POINT = _cv.CV_CALIB_FIX_PRINCIPAL_POINT
CV_CALIB_ZERO_TANGENT_DIST = _cv.CV_CALIB_ZERO_TANGENT_DIST
CV_CALIB_CB_ADAPTIVE_THRESH = _cv.CV_CALIB_CB_ADAPTIVE_THRESH
CV_CALIB_CB_NORMALIZE_IMAGE = _cv.CV_CALIB_CB_NORMALIZE_IMAGE
CV_CALIB_CB_FILTER_QUADS = _cv.CV_CALIB_CB_FILTER_QUADS
CV_FM_7POINT = _cv.CV_FM_7POINT
CV_FM_8POINT = _cv.CV_FM_8POINT
CV_FM_LMEDS_ONLY = _cv.CV_FM_LMEDS_ONLY
CV_FM_RANSAC_ONLY = _cv.CV_FM_RANSAC_ONLY
CV_FM_LMEDS = _cv.CV_FM_LMEDS
CV_FM_RANSAC = _cv.CV_FM_RANSAC
CV_RETR_EXTERNAL = _cv.CV_RETR_EXTERNAL
CV_RETR_LIST = _cv.CV_RETR_LIST
CV_RETR_CCOMP = _cv.CV_RETR_CCOMP
CV_RETR_TREE = _cv.CV_RETR_TREE
CV_CHAIN_CODE = _cv.CV_CHAIN_CODE
CV_CHAIN_APPROX_NONE = _cv.CV_CHAIN_APPROX_NONE
CV_CHAIN_APPROX_SIMPLE = _cv.CV_CHAIN_APPROX_SIMPLE
CV_CHAIN_APPROX_TC89_L1 = _cv.CV_CHAIN_APPROX_TC89_L1
CV_CHAIN_APPROX_TC89_KCOS = _cv.CV_CHAIN_APPROX_TC89_KCOS
CV_LINK_RUNS = _cv.CV_LINK_RUNS
CV_SUBDIV2D_VIRTUAL_POINT_FLAG = _cv.CV_SUBDIV2D_VIRTUAL_POINT_FLAG
CV_DIST_USER = _cv.CV_DIST_USER
CV_DIST_L1 = _cv.CV_DIST_L1
CV_DIST_L2 = _cv.CV_DIST_L2
CV_DIST_C = _cv.CV_DIST_C
CV_DIST_L12 = _cv.CV_DIST_L12
CV_DIST_FAIR = _cv.CV_DIST_FAIR
CV_DIST_WELSCH = _cv.CV_DIST_WELSCH
CV_DIST_HUBER = _cv.CV_DIST_HUBER
CV_HAAR_MAGIC_VAL = _cv.CV_HAAR_MAGIC_VAL
CV_TYPE_NAME_HAAR = _cv.CV_TYPE_NAME_HAAR
CV_HAAR_FEATURE_MAX = _cv.CV_HAAR_FEATURE_MAX
class Cv32suf(_object):
    """Proxy of C++ Cv32suf class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Cv32suf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Cv32suf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _cv.Cv32suf_i_set
    __swig_getmethods__["i"] = _cv.Cv32suf_i_get
    if _newclass:i = _swig_property(_cv.Cv32suf_i_get, _cv.Cv32suf_i_set)
    __swig_setmethods__["u"] = _cv.Cv32suf_u_set
    __swig_getmethods__["u"] = _cv.Cv32suf_u_get
    if _newclass:u = _swig_property(_cv.Cv32suf_u_get, _cv.Cv32suf_u_set)
    __swig_setmethods__["f"] = _cv.Cv32suf_f_set
    __swig_getmethods__["f"] = _cv.Cv32suf_f_get
    if _newclass:f = _swig_property(_cv.Cv32suf_f_get, _cv.Cv32suf_f_set)
    def __init__(self, *args): 
        """__init__(self) -> Cv32suf"""
        this = _cv.new_Cv32suf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_Cv32suf
    __del__ = lambda self : None;
Cv32suf_swigregister = _cv.Cv32suf_swigregister
Cv32suf_swigregister(Cv32suf)

def cvCvtSeqToArray(*args):
  """
    cvCvtSeqToArray(CvSeq seq, CvArr elements, CvSlice slice=CV_WHOLE_SEQ) -> CvArr
    cvCvtSeqToArray(CvSeq seq, CvArr elements) -> CvArr
    """
  return _cv.cvCvtSeqToArray(*args)

def cvArcLength(*args):
  """
    cvArcLength(CvSeq seq, CvSlice slice=CV_WHOLE_SEQ, int is_closed=-1) -> double
    cvArcLength(CvSeq seq, CvSlice slice=CV_WHOLE_SEQ) -> double
    cvArcLength(CvSeq seq) -> double
    cvArcLength(CvArr arr, CvSlice slice=CV_WHOLE_SEQ, int is_closed=-1) -> double
    cvArcLength(CvArr arr, CvSlice slice=CV_WHOLE_SEQ) -> double
    cvArcLength(CvArr arr) -> double
    """
  return _cv.cvArcLength(*args)

def cvContourPerimeter(*args):
  """
    cvContourPerimeter(CvSeq seq) -> double
    cvContourPerimeter(CvArr arr) -> double
    """
  return _cv.cvContourPerimeter(*args)

def cvHaarDetectObjects(*args):
  """
    cvHaarDetectObjects(CvArr image, CvHaarClassifierCascade cascade, CvMemStorage storage, 
        double scale_factor=1.1, int min_neighbors=3, 
        int flags=0, CvSize min_size=cvSize(0,0)) -> CvSeq_CvRect
    cvHaarDetectObjects(CvArr image, CvHaarClassifierCascade cascade, CvMemStorage storage, 
        double scale_factor=1.1, int min_neighbors=3, 
        int flags=0) -> CvSeq_CvRect
    cvHaarDetectObjects(CvArr image, CvHaarClassifierCascade cascade, CvMemStorage storage, 
        double scale_factor=1.1, int min_neighbors=3) -> CvSeq_CvRect
    cvHaarDetectObjects(CvArr image, CvHaarClassifierCascade cascade, CvMemStorage storage, 
        double scale_factor=1.1) -> CvSeq_CvRect
    cvHaarDetectObjects(CvArr image, CvHaarClassifierCascade cascade, CvMemStorage storage) -> CvSeq_CvRect
    """
  return _cv.cvHaarDetectObjects(*args)

def cvApproxPoly(*args):
  """
    cvApproxPoly(void src_seq, int header_size, CvMemStorage storage, 
        int method, double parameter, int parameter2=0) -> CvSeq_CvPoint
    cvApproxPoly(void src_seq, int header_size, CvMemStorage storage, 
        int method, double parameter) -> CvSeq_CvPoint
    """
  return _cv.cvApproxPoly(*args)

def cvConvexHull2(*args):
  """
    cvConvexHull2(CvArr points, int orientation=CV_CLOCKWISE, int return_points=0) -> CvMat
    cvConvexHull2(CvArr points, int orientation=CV_CLOCKWISE) -> CvMat
    cvConvexHull2(CvArr points) -> CvMat
    """
  return _cv.cvConvexHull2(*args)
cvar = _cv.cvar
icvDepthToType = cvar.icvDepthToType

class Cv64suf(_object):
    """Proxy of C++ Cv64suf class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Cv64suf, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Cv64suf, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _cv.Cv64suf_i_set
    __swig_getmethods__["i"] = _cv.Cv64suf_i_get
    if _newclass:i = _swig_property(_cv.Cv64suf_i_get, _cv.Cv64suf_i_set)
    __swig_setmethods__["u"] = _cv.Cv64suf_u_set
    __swig_getmethods__["u"] = _cv.Cv64suf_u_get
    if _newclass:u = _swig_property(_cv.Cv64suf_u_get, _cv.Cv64suf_u_set)
    __swig_setmethods__["f"] = _cv.Cv64suf_f_set
    __swig_getmethods__["f"] = _cv.Cv64suf_f_get
    if _newclass:f = _swig_property(_cv.Cv64suf_f_get, _cv.Cv64suf_f_set)
    def __init__(self, *args): 
        """__init__(self) -> Cv64suf"""
        this = _cv.new_Cv64suf(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_Cv64suf
    __del__ = lambda self : None;
Cv64suf_swigregister = _cv.Cv64suf_swigregister
Cv64suf_swigregister(Cv64suf)


def cvRound(*args):
  """cvRound(double value) -> int"""
  return _cv.cvRound(*args)

def cvFloor(*args):
  """cvFloor(double value) -> int"""
  return _cv.cvFloor(*args)

def cvCeil(*args):
  """cvCeil(double value) -> int"""
  return _cv.cvCeil(*args)

def cvIsNaN(*args):
  """cvIsNaN(double value) -> int"""
  return _cv.cvIsNaN(*args)

def cvIsInf(*args):
  """cvIsInf(double value) -> int"""
  return _cv.cvIsInf(*args)

def cvRandInt(*args):
  """cvRandInt(CvRNG rng) -> unsigned int"""
  return _cv.cvRandInt(*args)

def cvRandReal(*args):
  """cvRandReal(CvRNG rng) -> double"""
  return _cv.cvRandReal(*args)
class IplImage(_object):
    """Proxy of C++ IplImage class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IplImage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IplImage, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["ID"] = _cv.IplImage_ID_set
    __swig_getmethods__["ID"] = _cv.IplImage_ID_get
    if _newclass:ID = _swig_property(_cv.IplImage_ID_get, _cv.IplImage_ID_set)
    __swig_setmethods__["nChannels"] = _cv.IplImage_nChannels_set
    __swig_getmethods__["nChannels"] = _cv.IplImage_nChannels_get
    if _newclass:nChannels = _swig_property(_cv.IplImage_nChannels_get, _cv.IplImage_nChannels_set)
    __swig_setmethods__["depth"] = _cv.IplImage_depth_set
    __swig_getmethods__["depth"] = _cv.IplImage_depth_get
    if _newclass:depth = _swig_property(_cv.IplImage_depth_get, _cv.IplImage_depth_set)
    __swig_setmethods__["dataOrder"] = _cv.IplImage_dataOrder_set
    __swig_getmethods__["dataOrder"] = _cv.IplImage_dataOrder_get
    if _newclass:dataOrder = _swig_property(_cv.IplImage_dataOrder_get, _cv.IplImage_dataOrder_set)
    __swig_setmethods__["origin"] = _cv.IplImage_origin_set
    __swig_getmethods__["origin"] = _cv.IplImage_origin_get
    if _newclass:origin = _swig_property(_cv.IplImage_origin_get, _cv.IplImage_origin_set)
    __swig_setmethods__["align"] = _cv.IplImage_align_set
    __swig_getmethods__["align"] = _cv.IplImage_align_get
    if _newclass:align = _swig_property(_cv.IplImage_align_get, _cv.IplImage_align_set)
    __swig_setmethods__["width"] = _cv.IplImage_width_set
    __swig_getmethods__["width"] = _cv.IplImage_width_get
    if _newclass:width = _swig_property(_cv.IplImage_width_get, _cv.IplImage_width_set)
    __swig_setmethods__["height"] = _cv.IplImage_height_set
    __swig_getmethods__["height"] = _cv.IplImage_height_get
    if _newclass:height = _swig_property(_cv.IplImage_height_get, _cv.IplImage_height_set)
    __swig_setmethods__["roi"] = _cv.IplImage_roi_set
    __swig_getmethods__["roi"] = _cv.IplImage_roi_get
    if _newclass:roi = _swig_property(_cv.IplImage_roi_get, _cv.IplImage_roi_set)
    __swig_setmethods__["imageSize"] = _cv.IplImage_imageSize_set
    __swig_getmethods__["imageSize"] = _cv.IplImage_imageSize_get
    if _newclass:imageSize = _swig_property(_cv.IplImage_imageSize_get, _cv.IplImage_imageSize_set)
    __swig_setmethods__["widthStep"] = _cv.IplImage_widthStep_set
    __swig_getmethods__["widthStep"] = _cv.IplImage_widthStep_get
    if _newclass:widthStep = _swig_property(_cv.IplImage_widthStep_get, _cv.IplImage_widthStep_set)
    __swig_destroy__ = _cv.delete_IplImage
    __del__ = lambda self : None;
    def __mul__(*args):
        """__mul__(self, CvArr src)"""
        return _cv.IplImage___mul__(*args)

    def __imul__(*args):
        """__imul__(self, CvArr src)"""
        return _cv.IplImage___imul__(*args)

    def __idiv__(*args):
        """__idiv__(self, CvArr src)"""
        return _cv.IplImage___idiv__(*args)

    def __add__(*args):
        """
        __add__(self, CvArr src)
        __add__(self, CvScalar val)
        """
        return _cv.IplImage___add__(*args)

    def __iadd__(*args):
        """
        __iadd__(self, CvArr src)
        __iadd__(self, CvScalar val)
        """
        return _cv.IplImage___iadd__(*args)

    def __xor__(*args):
        """
        __xor__(self, CvArr src)
        __xor__(self, CvScalar val)
        """
        return _cv.IplImage___xor__(*args)

    def __ixor__(*args):
        """
        __ixor__(self, CvArr src)
        __ixor__(self, CvScalar val)
        """
        return _cv.IplImage___ixor__(*args)

    def __sub__(*args):
        """
        __sub__(self, CvArr src)
        __sub__(self, CvScalar val)
        """
        return _cv.IplImage___sub__(*args)

    def __isub__(*args):
        """
        __isub__(self, CvArr src)
        __isub__(self, CvScalar val)
        """
        return _cv.IplImage___isub__(*args)

    def __or__(*args):
        """
        __or__(self, CvArr src)
        __or__(self, CvScalar val)
        """
        return _cv.IplImage___or__(*args)

    def __ior__(*args):
        """
        __ior__(self, CvArr src)
        __ior__(self, CvScalar val)
        """
        return _cv.IplImage___ior__(*args)

    def __and__(*args):
        """
        __and__(self, CvArr src)
        __and__(self, CvScalar val)
        """
        return _cv.IplImage___and__(*args)

    def __iand__(*args):
        """
        __iand__(self, CvArr src)
        __iand__(self, CvScalar val)
        """
        return _cv.IplImage___iand__(*args)

    def __ge__(*args):
        """
        __ge__(self, CvArr src)
        __ge__(self, double val)
        """
        return _cv.IplImage___ge__(*args)

    def __eq__(*args):
        """
        __eq__(self, CvArr src)
        __eq__(self, double val)
        """
        return _cv.IplImage___eq__(*args)

    def __le__(*args):
        """
        __le__(self, CvArr src)
        __le__(self, double val)
        """
        return _cv.IplImage___le__(*args)

    def __ne__(*args):
        """
        __ne__(self, CvArr src)
        __ne__(self, double val)
        """
        return _cv.IplImage___ne__(*args)

    def __lt__(*args):
        """
        __lt__(self, CvArr src)
        __lt__(self, double val)
        """
        return _cv.IplImage___lt__(*args)

    def __gt__(*args):
        """
        __gt__(self, CvArr src)
        __gt__(self, double val)
        """
        return _cv.IplImage___gt__(*args)

    def __div__(*args):
        """
        __div__(self, CvArr src)
        __div__(self, double val)
        """
        return _cv.IplImage___div__(*args)

    def __radd__(*args):
        """
        __radd__(self, CvArr arg)
        __radd__(self, CvScalar arg)
        __radd__(self, double arg)
        """
        return _cv.IplImage___radd__(*args)

    def __rsub__(*args):
        """
        __rsub__(self, CvArr arg)
        __rsub__(self, CvScalar arg)
        __rsub__(self, double arg)
        """
        return _cv.IplImage___rsub__(*args)

    def __rmul__(*args):
        """
        __rmul__(self, CvArr arg)
        __rmul__(self, double arg) -> CvArr
        """
        return _cv.IplImage___rmul__(*args)

    def __rdiv__(*args):
        """
        __rdiv__(self, CvArr arg)
        __rdiv__(self, double arg) -> CvArr
        """
        return _cv.IplImage___rdiv__(*args)

    def __ror__(*args):
        """
        __ror__(self, CvScalar arg)
        __ror__(self, double arg)
        """
        return _cv.IplImage___ror__(*args)

    def __rand__(*args):
        """
        __rand__(self, CvScalar arg)
        __rand__(self, double arg)
        """
        return _cv.IplImage___rand__(*args)

    def __rxor__(*args):
        """
        __rxor__(self, CvScalar arg)
        __rxor__(self, double arg)
        """
        return _cv.IplImage___rxor__(*args)

    def __req__(*args):
        """__req__(self, double arg) -> CvArr"""
        return _cv.IplImage___req__(*args)

    def __rgt__(*args):
        """__rgt__(self, double arg) -> CvArr"""
        return _cv.IplImage___rgt__(*args)

    def __rge__(*args):
        """__rge__(self, double arg) -> CvArr"""
        return _cv.IplImage___rge__(*args)

    def __rlt__(*args):
        """__rlt__(self, double arg) -> CvArr"""
        return _cv.IplImage___rlt__(*args)

    def __rle__(*args):
        """__rle__(self, double arg) -> CvArr"""
        return _cv.IplImage___rle__(*args)

    def __rne__(*args):
        """__rne__(self, double arg) -> CvArr"""
        return _cv.IplImage___rne__(*args)

    def __pow__(*args):
        """__pow__(self, double arg)"""
        return _cv.IplImage___pow__(*args)

    def __str__(*args):
        """__str__(self) -> char"""
        return _cv.IplImage___str__(*args)

    def __setitem__(*args):
        """
        __setitem__(self, PyObject object, double val)
        __setitem__(self, PyObject object, CvPoint val)
        __setitem__(self, PyObject object, CvPoint2D32f val)
        __setitem__(self, PyObject object, CvScalar val)
        __setitem__(self, PyObject object, CvArr arr)
        """
        return _cv.IplImage___setitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, PyObject object) -> PyObject"""
        return _cv.IplImage___getitem__(*args)

IplImage_swigregister = _cv.IplImage_swigregister
IplImage_swigregister(IplImage)

def cvRNG(*args):
  """
    cvRNG(int64 seed=-1) -> CvRNG
    cvRNG() -> CvRNG
    """
  return _cv.cvRNG(*args)

class IplROI(_object):
    """Proxy of C++ IplROI class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IplROI, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IplROI, name)
    __repr__ = _swig_repr
    __swig_setmethods__["coi"] = _cv.IplROI_coi_set
    __swig_getmethods__["coi"] = _cv.IplROI_coi_get
    if _newclass:coi = _swig_property(_cv.IplROI_coi_get, _cv.IplROI_coi_set)
    __swig_setmethods__["xOffset"] = _cv.IplROI_xOffset_set
    __swig_getmethods__["xOffset"] = _cv.IplROI_xOffset_get
    if _newclass:xOffset = _swig_property(_cv.IplROI_xOffset_get, _cv.IplROI_xOffset_set)
    __swig_setmethods__["yOffset"] = _cv.IplROI_yOffset_set
    __swig_getmethods__["yOffset"] = _cv.IplROI_yOffset_get
    if _newclass:yOffset = _swig_property(_cv.IplROI_yOffset_get, _cv.IplROI_yOffset_set)
    __swig_setmethods__["width"] = _cv.IplROI_width_set
    __swig_getmethods__["width"] = _cv.IplROI_width_get
    if _newclass:width = _swig_property(_cv.IplROI_width_get, _cv.IplROI_width_set)
    __swig_setmethods__["height"] = _cv.IplROI_height_set
    __swig_getmethods__["height"] = _cv.IplROI_height_get
    if _newclass:height = _swig_property(_cv.IplROI_height_get, _cv.IplROI_height_set)
    def __init__(self, *args): 
        """__init__(self) -> IplROI"""
        this = _cv.new_IplROI(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_IplROI
    __del__ = lambda self : None;
IplROI_swigregister = _cv.IplROI_swigregister
IplROI_swigregister(IplROI)

class IplConvKernel(_object):
    """Proxy of C++ IplConvKernel class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IplConvKernel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IplConvKernel, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["nCols"] = _cv.IplConvKernel_nCols_set
    __swig_getmethods__["nCols"] = _cv.IplConvKernel_nCols_get
    if _newclass:nCols = _swig_property(_cv.IplConvKernel_nCols_get, _cv.IplConvKernel_nCols_set)
    __swig_setmethods__["nRows"] = _cv.IplConvKernel_nRows_set
    __swig_getmethods__["nRows"] = _cv.IplConvKernel_nRows_get
    if _newclass:nRows = _swig_property(_cv.IplConvKernel_nRows_get, _cv.IplConvKernel_nRows_set)
    __swig_setmethods__["anchorX"] = _cv.IplConvKernel_anchorX_set
    __swig_getmethods__["anchorX"] = _cv.IplConvKernel_anchorX_get
    if _newclass:anchorX = _swig_property(_cv.IplConvKernel_anchorX_get, _cv.IplConvKernel_anchorX_set)
    __swig_setmethods__["anchorY"] = _cv.IplConvKernel_anchorY_set
    __swig_getmethods__["anchorY"] = _cv.IplConvKernel_anchorY_get
    if _newclass:anchorY = _swig_property(_cv.IplConvKernel_anchorY_get, _cv.IplConvKernel_anchorY_set)
    __swig_setmethods__["values"] = _cv.IplConvKernel_values_set
    __swig_getmethods__["values"] = _cv.IplConvKernel_values_get
    if _newclass:values = _swig_property(_cv.IplConvKernel_values_get, _cv.IplConvKernel_values_set)
    __swig_setmethods__["nShiftR"] = _cv.IplConvKernel_nShiftR_set
    __swig_getmethods__["nShiftR"] = _cv.IplConvKernel_nShiftR_get
    if _newclass:nShiftR = _swig_property(_cv.IplConvKernel_nShiftR_get, _cv.IplConvKernel_nShiftR_set)
    __swig_destroy__ = _cv.delete_IplConvKernel
    __del__ = lambda self : None;
IplConvKernel_swigregister = _cv.IplConvKernel_swigregister
IplConvKernel_swigregister(IplConvKernel)

class IplConvKernelFP(_object):
    """Proxy of C++ IplConvKernelFP class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IplConvKernelFP, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IplConvKernelFP, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nCols"] = _cv.IplConvKernelFP_nCols_set
    __swig_getmethods__["nCols"] = _cv.IplConvKernelFP_nCols_get
    if _newclass:nCols = _swig_property(_cv.IplConvKernelFP_nCols_get, _cv.IplConvKernelFP_nCols_set)
    __swig_setmethods__["nRows"] = _cv.IplConvKernelFP_nRows_set
    __swig_getmethods__["nRows"] = _cv.IplConvKernelFP_nRows_get
    if _newclass:nRows = _swig_property(_cv.IplConvKernelFP_nRows_get, _cv.IplConvKernelFP_nRows_set)
    __swig_setmethods__["anchorX"] = _cv.IplConvKernelFP_anchorX_set
    __swig_getmethods__["anchorX"] = _cv.IplConvKernelFP_anchorX_get
    if _newclass:anchorX = _swig_property(_cv.IplConvKernelFP_anchorX_get, _cv.IplConvKernelFP_anchorX_set)
    __swig_setmethods__["anchorY"] = _cv.IplConvKernelFP_anchorY_set
    __swig_getmethods__["anchorY"] = _cv.IplConvKernelFP_anchorY_get
    if _newclass:anchorY = _swig_property(_cv.IplConvKernelFP_anchorY_get, _cv.IplConvKernelFP_anchorY_set)
    __swig_setmethods__["values"] = _cv.IplConvKernelFP_values_set
    __swig_getmethods__["values"] = _cv.IplConvKernelFP_values_get
    if _newclass:values = _swig_property(_cv.IplConvKernelFP_values_get, _cv.IplConvKernelFP_values_set)
    def __init__(self, *args): 
        """__init__(self) -> IplConvKernelFP"""
        this = _cv.new_IplConvKernelFP(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_IplConvKernelFP
    __del__ = lambda self : None;
IplConvKernelFP_swigregister = _cv.IplConvKernelFP_swigregister
IplConvKernelFP_swigregister(IplConvKernelFP)

class CvMat(_object):
    """Proxy of C++ CvMat class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMat, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _cv.CvMat_type_set
    __swig_getmethods__["type"] = _cv.CvMat_type_get
    if _newclass:type = _swig_property(_cv.CvMat_type_get, _cv.CvMat_type_set)
    __swig_setmethods__["step"] = _cv.CvMat_step_set
    __swig_getmethods__["step"] = _cv.CvMat_step_get
    if _newclass:step = _swig_property(_cv.CvMat_step_get, _cv.CvMat_step_set)
    __swig_setmethods__["refcount"] = _cv.CvMat_refcount_set
    __swig_getmethods__["refcount"] = _cv.CvMat_refcount_get
    if _newclass:refcount = _swig_property(_cv.CvMat_refcount_get, _cv.CvMat_refcount_set)
    __swig_setmethods__["hdr_refcount"] = _cv.CvMat_hdr_refcount_set
    __swig_getmethods__["hdr_refcount"] = _cv.CvMat_hdr_refcount_get
    if _newclass:hdr_refcount = _swig_property(_cv.CvMat_hdr_refcount_get, _cv.CvMat_hdr_refcount_set)
    __swig_getmethods__["data"] = _cv.CvMat_data_get
    if _newclass:data = _swig_property(_cv.CvMat_data_get)
    __swig_destroy__ = _cv.delete_CvMat
    __del__ = lambda self : None;
    __swig_getmethods__["depth"] = _cv.CvMat_depth_get
    if _newclass:depth = _swig_property(_cv.CvMat_depth_get)
    __swig_getmethods__["nChannels"] = _cv.CvMat_nChannels_get
    if _newclass:nChannels = _swig_property(_cv.CvMat_nChannels_get)
    __swig_getmethods__["dataOrder"] = _cv.CvMat_dataOrder_get
    if _newclass:dataOrder = _swig_property(_cv.CvMat_dataOrder_get)
    __swig_getmethods__["origin"] = _cv.CvMat_origin_get
    if _newclass:origin = _swig_property(_cv.CvMat_origin_get)
    __swig_getmethods__["width"] = _cv.CvMat_width_get
    if _newclass:width = _swig_property(_cv.CvMat_width_get)
    __swig_getmethods__["height"] = _cv.CvMat_height_get
    if _newclass:height = _swig_property(_cv.CvMat_height_get)
    __swig_getmethods__["imageSize"] = _cv.CvMat_imageSize_get
    if _newclass:imageSize = _swig_property(_cv.CvMat_imageSize_get)
    __swig_getmethods__["widthStep"] = _cv.CvMat_widthStep_get
    if _newclass:widthStep = _swig_property(_cv.CvMat_widthStep_get)
    __swig_getmethods__["rows"] = _cv.CvMat_rows_get
    if _newclass:rows = _swig_property(_cv.CvMat_rows_get)
    __swig_getmethods__["cols"] = _cv.CvMat_cols_get
    if _newclass:cols = _swig_property(_cv.CvMat_cols_get)
    def __mul__(*args):
        """__mul__(self, CvArr src) -> CvMat"""
        return _cv.CvMat___mul__(*args)

    def __imul__(*args):
        """__imul__(self, CvArr src) -> CvMat"""
        return _cv.CvMat___imul__(*args)

    def __idiv__(*args):
        """__idiv__(self, CvArr src) -> CvMat"""
        return _cv.CvMat___idiv__(*args)

    def __add__(*args):
        """
        __add__(self, CvArr src) -> CvMat
        __add__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___add__(*args)

    def __iadd__(*args):
        """
        __iadd__(self, CvArr src) -> CvMat
        __iadd__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___iadd__(*args)

    def __xor__(*args):
        """
        __xor__(self, CvArr src) -> CvMat
        __xor__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___xor__(*args)

    def __ixor__(*args):
        """
        __ixor__(self, CvArr src) -> CvMat
        __ixor__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___ixor__(*args)

    def __sub__(*args):
        """
        __sub__(self, CvArr src) -> CvMat
        __sub__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___sub__(*args)

    def __isub__(*args):
        """
        __isub__(self, CvArr src) -> CvMat
        __isub__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___isub__(*args)

    def __or__(*args):
        """
        __or__(self, CvArr src) -> CvMat
        __or__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___or__(*args)

    def __ior__(*args):
        """
        __ior__(self, CvArr src) -> CvMat
        __ior__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___ior__(*args)

    def __and__(*args):
        """
        __and__(self, CvArr src) -> CvMat
        __and__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___and__(*args)

    def __iand__(*args):
        """
        __iand__(self, CvArr src) -> CvMat
        __iand__(self, CvScalar val) -> CvMat
        """
        return _cv.CvMat___iand__(*args)

    def __ge__(*args):
        """
        __ge__(self, CvArr src) -> CvMat
        __ge__(self, double val) -> CvMat
        """
        return _cv.CvMat___ge__(*args)

    def __eq__(*args):
        """
        __eq__(self, CvArr src) -> CvMat
        __eq__(self, double val) -> CvMat
        """
        return _cv.CvMat___eq__(*args)

    def __le__(*args):
        """
        __le__(self, CvArr src) -> CvMat
        __le__(self, double val) -> CvMat
        """
        return _cv.CvMat___le__(*args)

    def __ne__(*args):
        """
        __ne__(self, CvArr src) -> CvMat
        __ne__(self, double val) -> CvMat
        """
        return _cv.CvMat___ne__(*args)

    def __lt__(*args):
        """
        __lt__(self, CvArr src) -> CvMat
        __lt__(self, double val) -> CvMat
        """
        return _cv.CvMat___lt__(*args)

    def __gt__(*args):
        """
        __gt__(self, CvArr src) -> CvMat
        __gt__(self, double val) -> CvMat
        """
        return _cv.CvMat___gt__(*args)

    def __div__(*args):
        """
        __div__(self, CvArr src) -> CvMat
        __div__(self, double val) -> CvMat
        """
        return _cv.CvMat___div__(*args)

    def __radd__(*args):
        """
        __radd__(self, CvArr arg) -> CvMat
        __radd__(self, CvScalar arg) -> CvMat
        __radd__(self, double arg) -> CvMat
        """
        return _cv.CvMat___radd__(*args)

    def __rsub__(*args):
        """
        __rsub__(self, CvArr arg) -> CvMat
        __rsub__(self, CvScalar arg) -> CvMat
        __rsub__(self, double arg) -> CvMat
        """
        return _cv.CvMat___rsub__(*args)

    def __rmul__(*args):
        """
        __rmul__(self, CvArr arg) -> CvMat
        __rmul__(self, double arg) -> CvArr
        """
        return _cv.CvMat___rmul__(*args)

    def __rdiv__(*args):
        """
        __rdiv__(self, CvArr arg) -> CvMat
        __rdiv__(self, double arg) -> CvArr
        """
        return _cv.CvMat___rdiv__(*args)

    def __ror__(*args):
        """
        __ror__(self, CvScalar arg) -> CvMat
        __ror__(self, double arg) -> CvMat
        """
        return _cv.CvMat___ror__(*args)

    def __rand__(*args):
        """
        __rand__(self, CvScalar arg) -> CvMat
        __rand__(self, double arg) -> CvMat
        """
        return _cv.CvMat___rand__(*args)

    def __rxor__(*args):
        """
        __rxor__(self, CvScalar arg) -> CvMat
        __rxor__(self, double arg) -> CvMat
        """
        return _cv.CvMat___rxor__(*args)

    def __req__(*args):
        """__req__(self, double arg) -> CvArr"""
        return _cv.CvMat___req__(*args)

    def __rgt__(*args):
        """__rgt__(self, double arg) -> CvArr"""
        return _cv.CvMat___rgt__(*args)

    def __rge__(*args):
        """__rge__(self, double arg) -> CvArr"""
        return _cv.CvMat___rge__(*args)

    def __rlt__(*args):
        """__rlt__(self, double arg) -> CvArr"""
        return _cv.CvMat___rlt__(*args)

    def __rle__(*args):
        """__rle__(self, double arg) -> CvArr"""
        return _cv.CvMat___rle__(*args)

    def __rne__(*args):
        """__rne__(self, double arg) -> CvArr"""
        return _cv.CvMat___rne__(*args)

    def __pow__(*args):
        """__pow__(self, double arg) -> CvMat"""
        return _cv.CvMat___pow__(*args)

    def __str__(*args):
        """__str__(self) -> char"""
        return _cv.CvMat___str__(*args)

    def __setitem__(*args):
        """
        __setitem__(self, PyObject object, double val)
        __setitem__(self, PyObject object, CvPoint val)
        __setitem__(self, PyObject object, CvPoint2D32f val)
        __setitem__(self, PyObject object, CvScalar val)
        __setitem__(self, PyObject object, CvArr arr)
        """
        return _cv.CvMat___setitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, PyObject object) -> PyObject"""
        return _cv.CvMat___getitem__(*args)

    def __iter__(self):
       	"""
       	generator function iterating through rows in matrix or elements in vector
       	"""
    	if self.rows==1:
    		return self.colrange()
    	return self.rowrange()

    def rowrange(self):
        """
        generator function iterating along rows in matrix
        """
    	for i in range(self.rows):
    		yield self[i]

    def colrange(self):
        """
        generator function iterating along columns in matrix
        """
    	for i in range(self.cols):
    		yield self[:,i]

    # if arg is None, python still calls our operator overloads
    # but we want
    # if mat != None
    # if mat == None
    # to do the right thing -- so redefine __ne__ and __eq__

    def __eq__(self, arg):
        """
    	__eq__(self, None)
    	__eq__(self, CvArr src)
    	__eq__(self, double val)
        """

    	if not arg:
    		return False 
    	return _cv.CvMat___eq__(self, arg)
    def __ne__(self, arg):
        """
    	__ne__(self, None)
    	__ne__(self, CvArr src)
    	__ne__(self, double val)
        """

    	if not arg:
    		return True
    	return _cv.CvMat___ne__(self, arg)

    __swig_setmethods__["imageData"] = _cv.CvMat_imageData_set
    __swig_getmethods__["imageData"] = _cv.CvMat_imageData_get
    if _newclass:imageData = _swig_property(_cv.CvMat_imageData_get, _cv.CvMat_imageData_set)
CvMat_swigregister = _cv.CvMat_swigregister
CvMat_swigregister(CvMat)

class CvMat_data(_object):
    """Proxy of C++ CvMat_data class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMat_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMat_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ptr"] = _cv.CvMat_data_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvMat_data_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvMat_data_ptr_get, _cv.CvMat_data_ptr_set)
    __swig_setmethods__["s"] = _cv.CvMat_data_s_set
    __swig_getmethods__["s"] = _cv.CvMat_data_s_get
    if _newclass:s = _swig_property(_cv.CvMat_data_s_get, _cv.CvMat_data_s_set)
    __swig_setmethods__["i"] = _cv.CvMat_data_i_set
    __swig_getmethods__["i"] = _cv.CvMat_data_i_get
    if _newclass:i = _swig_property(_cv.CvMat_data_i_get, _cv.CvMat_data_i_set)
    __swig_setmethods__["fl"] = _cv.CvMat_data_fl_set
    __swig_getmethods__["fl"] = _cv.CvMat_data_fl_get
    if _newclass:fl = _swig_property(_cv.CvMat_data_fl_get, _cv.CvMat_data_fl_set)
    __swig_setmethods__["db"] = _cv.CvMat_data_db_set
    __swig_getmethods__["db"] = _cv.CvMat_data_db_get
    if _newclass:db = _swig_property(_cv.CvMat_data_db_get, _cv.CvMat_data_db_set)
    def __init__(self, *args): 
        """__init__(self) -> CvMat_data"""
        this = _cv.new_CvMat_data(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMat_data
    __del__ = lambda self : None;
CvMat_data_swigregister = _cv.CvMat_data_swigregister
CvMat_data_swigregister(CvMat_data)


def cvmGet(*args):
  """cvmGet(CvMat mat, int row, int col) -> double"""
  return _cv.cvmGet(*args)

def cvmSet(*args):
  """cvmSet(CvMat mat, int row, int col, double value)"""
  return _cv.cvmSet(*args)

def cvCvToIplDepth(*args):
  """cvCvToIplDepth(int type) -> int"""
  return _cv.cvCvToIplDepth(*args)
class CvMatND(_object):
    """Proxy of C++ CvMatND class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMatND, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMatND, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _cv.CvMatND_type_set
    __swig_getmethods__["type"] = _cv.CvMatND_type_get
    if _newclass:type = _swig_property(_cv.CvMatND_type_get, _cv.CvMatND_type_set)
    __swig_setmethods__["dims"] = _cv.CvMatND_dims_set
    __swig_getmethods__["dims"] = _cv.CvMatND_dims_get
    if _newclass:dims = _swig_property(_cv.CvMatND_dims_get, _cv.CvMatND_dims_set)
    __swig_setmethods__["refcount"] = _cv.CvMatND_refcount_set
    __swig_getmethods__["refcount"] = _cv.CvMatND_refcount_get
    if _newclass:refcount = _swig_property(_cv.CvMatND_refcount_get, _cv.CvMatND_refcount_set)
    __swig_setmethods__["hdr_refcount"] = _cv.CvMatND_hdr_refcount_set
    __swig_getmethods__["hdr_refcount"] = _cv.CvMatND_hdr_refcount_get
    if _newclass:hdr_refcount = _swig_property(_cv.CvMatND_hdr_refcount_get, _cv.CvMatND_hdr_refcount_set)
    __swig_getmethods__["dim"] = _cv.CvMatND_dim_get
    if _newclass:dim = _swig_property(_cv.CvMatND_dim_get)
    __swig_getmethods__["data"] = _cv.CvMatND_data_get
    if _newclass:data = _swig_property(_cv.CvMatND_data_get)
    __swig_destroy__ = _cv.delete_CvMatND
    __del__ = lambda self : None;
CvMatND_swigregister = _cv.CvMatND_swigregister
CvMatND_swigregister(CvMatND)

def cvMat(*args):
  """
    cvMat(int rows, int cols, int type, void data=None) -> CvMat
    cvMat(int rows, int cols, int type) -> CvMat
    """
  return _cv.cvMat(*args)

class CvMatND_dim(_object):
    """Proxy of C++ CvMatND_dim class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMatND_dim, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMatND_dim, name)
    __repr__ = _swig_repr
    __swig_setmethods__["size"] = _cv.CvMatND_dim_size_set
    __swig_getmethods__["size"] = _cv.CvMatND_dim_size_get
    if _newclass:size = _swig_property(_cv.CvMatND_dim_size_get, _cv.CvMatND_dim_size_set)
    __swig_setmethods__["step"] = _cv.CvMatND_dim_step_set
    __swig_getmethods__["step"] = _cv.CvMatND_dim_step_get
    if _newclass:step = _swig_property(_cv.CvMatND_dim_step_get, _cv.CvMatND_dim_step_set)
    def __init__(self, *args): 
        """__init__(self) -> CvMatND_dim"""
        this = _cv.new_CvMatND_dim(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMatND_dim
    __del__ = lambda self : None;
CvMatND_dim_swigregister = _cv.CvMatND_dim_swigregister
CvMatND_dim_swigregister(CvMatND_dim)

class CvMatND_data(_object):
    """Proxy of C++ CvMatND_data class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMatND_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMatND_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ptr"] = _cv.CvMatND_data_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvMatND_data_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvMatND_data_ptr_get, _cv.CvMatND_data_ptr_set)
    __swig_setmethods__["fl"] = _cv.CvMatND_data_fl_set
    __swig_getmethods__["fl"] = _cv.CvMatND_data_fl_get
    if _newclass:fl = _swig_property(_cv.CvMatND_data_fl_get, _cv.CvMatND_data_fl_set)
    __swig_setmethods__["db"] = _cv.CvMatND_data_db_set
    __swig_getmethods__["db"] = _cv.CvMatND_data_db_get
    if _newclass:db = _swig_property(_cv.CvMatND_data_db_get, _cv.CvMatND_data_db_set)
    __swig_setmethods__["i"] = _cv.CvMatND_data_i_set
    __swig_getmethods__["i"] = _cv.CvMatND_data_i_get
    if _newclass:i = _swig_property(_cv.CvMatND_data_i_get, _cv.CvMatND_data_i_set)
    __swig_setmethods__["s"] = _cv.CvMatND_data_s_set
    __swig_getmethods__["s"] = _cv.CvMatND_data_s_get
    if _newclass:s = _swig_property(_cv.CvMatND_data_s_get, _cv.CvMatND_data_s_set)
    def __init__(self, *args): 
        """__init__(self) -> CvMatND_data"""
        this = _cv.new_CvMatND_data(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMatND_data
    __del__ = lambda self : None;
CvMatND_data_swigregister = _cv.CvMatND_data_swigregister
CvMatND_data_swigregister(CvMatND_data)

class CvSparseMat(_object):
    """Proxy of C++ CvSparseMat class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSparseMat, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSparseMat, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _cv.CvSparseMat_type_set
    __swig_getmethods__["type"] = _cv.CvSparseMat_type_get
    if _newclass:type = _swig_property(_cv.CvSparseMat_type_get, _cv.CvSparseMat_type_set)
    __swig_setmethods__["dims"] = _cv.CvSparseMat_dims_set
    __swig_getmethods__["dims"] = _cv.CvSparseMat_dims_get
    if _newclass:dims = _swig_property(_cv.CvSparseMat_dims_get, _cv.CvSparseMat_dims_set)
    __swig_setmethods__["refcount"] = _cv.CvSparseMat_refcount_set
    __swig_getmethods__["refcount"] = _cv.CvSparseMat_refcount_get
    if _newclass:refcount = _swig_property(_cv.CvSparseMat_refcount_get, _cv.CvSparseMat_refcount_set)
    __swig_setmethods__["hdr_refcount"] = _cv.CvSparseMat_hdr_refcount_set
    __swig_getmethods__["hdr_refcount"] = _cv.CvSparseMat_hdr_refcount_get
    if _newclass:hdr_refcount = _swig_property(_cv.CvSparseMat_hdr_refcount_get, _cv.CvSparseMat_hdr_refcount_set)
    __swig_setmethods__["heap"] = _cv.CvSparseMat_heap_set
    __swig_getmethods__["heap"] = _cv.CvSparseMat_heap_get
    if _newclass:heap = _swig_property(_cv.CvSparseMat_heap_get, _cv.CvSparseMat_heap_set)
    __swig_setmethods__["hashtable"] = _cv.CvSparseMat_hashtable_set
    __swig_getmethods__["hashtable"] = _cv.CvSparseMat_hashtable_get
    if _newclass:hashtable = _swig_property(_cv.CvSparseMat_hashtable_get, _cv.CvSparseMat_hashtable_set)
    __swig_setmethods__["hashsize"] = _cv.CvSparseMat_hashsize_set
    __swig_getmethods__["hashsize"] = _cv.CvSparseMat_hashsize_get
    if _newclass:hashsize = _swig_property(_cv.CvSparseMat_hashsize_get, _cv.CvSparseMat_hashsize_set)
    __swig_setmethods__["valoffset"] = _cv.CvSparseMat_valoffset_set
    __swig_getmethods__["valoffset"] = _cv.CvSparseMat_valoffset_get
    if _newclass:valoffset = _swig_property(_cv.CvSparseMat_valoffset_get, _cv.CvSparseMat_valoffset_set)
    __swig_setmethods__["idxoffset"] = _cv.CvSparseMat_idxoffset_set
    __swig_getmethods__["idxoffset"] = _cv.CvSparseMat_idxoffset_get
    if _newclass:idxoffset = _swig_property(_cv.CvSparseMat_idxoffset_get, _cv.CvSparseMat_idxoffset_set)
    __swig_setmethods__["size"] = _cv.CvSparseMat_size_set
    __swig_getmethods__["size"] = _cv.CvSparseMat_size_get
    if _newclass:size = _swig_property(_cv.CvSparseMat_size_get, _cv.CvSparseMat_size_set)
    __swig_destroy__ = _cv.delete_CvSparseMat
    __del__ = lambda self : None;
CvSparseMat_swigregister = _cv.CvSparseMat_swigregister
CvSparseMat_swigregister(CvSparseMat)

class CvSparseNode(_object):
    """Proxy of C++ CvSparseNode class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSparseNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSparseNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hashval"] = _cv.CvSparseNode_hashval_set
    __swig_getmethods__["hashval"] = _cv.CvSparseNode_hashval_get
    if _newclass:hashval = _swig_property(_cv.CvSparseNode_hashval_get, _cv.CvSparseNode_hashval_set)
    __swig_setmethods__["next"] = _cv.CvSparseNode_next_set
    __swig_getmethods__["next"] = _cv.CvSparseNode_next_get
    if _newclass:next = _swig_property(_cv.CvSparseNode_next_get, _cv.CvSparseNode_next_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSparseNode"""
        this = _cv.new_CvSparseNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSparseNode
    __del__ = lambda self : None;
CvSparseNode_swigregister = _cv.CvSparseNode_swigregister
CvSparseNode_swigregister(CvSparseNode)

class CvSparseMatIterator(_object):
    """Proxy of C++ CvSparseMatIterator class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSparseMatIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSparseMatIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mat"] = _cv.CvSparseMatIterator_mat_set
    __swig_getmethods__["mat"] = _cv.CvSparseMatIterator_mat_get
    if _newclass:mat = _swig_property(_cv.CvSparseMatIterator_mat_get, _cv.CvSparseMatIterator_mat_set)
    __swig_setmethods__["node"] = _cv.CvSparseMatIterator_node_set
    __swig_getmethods__["node"] = _cv.CvSparseMatIterator_node_get
    if _newclass:node = _swig_property(_cv.CvSparseMatIterator_node_get, _cv.CvSparseMatIterator_node_set)
    __swig_setmethods__["curidx"] = _cv.CvSparseMatIterator_curidx_set
    __swig_getmethods__["curidx"] = _cv.CvSparseMatIterator_curidx_get
    if _newclass:curidx = _swig_property(_cv.CvSparseMatIterator_curidx_get, _cv.CvSparseMatIterator_curidx_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSparseMatIterator"""
        this = _cv.new_CvSparseMatIterator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSparseMatIterator
    __del__ = lambda self : None;
CvSparseMatIterator_swigregister = _cv.CvSparseMatIterator_swigregister
CvSparseMatIterator_swigregister(CvSparseMatIterator)

class CvHistogram(_object):
    """Proxy of C++ CvHistogram class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvHistogram, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvHistogram, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _cv.CvHistogram_type_set
    __swig_getmethods__["type"] = _cv.CvHistogram_type_get
    if _newclass:type = _swig_property(_cv.CvHistogram_type_get, _cv.CvHistogram_type_set)
    __swig_setmethods__["bins"] = _cv.CvHistogram_bins_set
    __swig_getmethods__["bins"] = _cv.CvHistogram_bins_get
    if _newclass:bins = _swig_property(_cv.CvHistogram_bins_get, _cv.CvHistogram_bins_set)
    __swig_setmethods__["thresh"] = _cv.CvHistogram_thresh_set
    __swig_getmethods__["thresh"] = _cv.CvHistogram_thresh_get
    if _newclass:thresh = _swig_property(_cv.CvHistogram_thresh_get, _cv.CvHistogram_thresh_set)
    __swig_setmethods__["thresh2"] = _cv.CvHistogram_thresh2_set
    __swig_getmethods__["thresh2"] = _cv.CvHistogram_thresh2_get
    if _newclass:thresh2 = _swig_property(_cv.CvHistogram_thresh2_get, _cv.CvHistogram_thresh2_set)
    __swig_setmethods__["mat"] = _cv.CvHistogram_mat_set
    __swig_getmethods__["mat"] = _cv.CvHistogram_mat_get
    if _newclass:mat = _swig_property(_cv.CvHistogram_mat_get, _cv.CvHistogram_mat_set)
    __swig_destroy__ = _cv.delete_CvHistogram
    __del__ = lambda self : None;
CvHistogram_swigregister = _cv.CvHistogram_swigregister
CvHistogram_swigregister(CvHistogram)

class CvRect(_object):
    """Proxy of C++ CvRect class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvRect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvRect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _cv.CvRect_x_set
    __swig_getmethods__["x"] = _cv.CvRect_x_get
    if _newclass:x = _swig_property(_cv.CvRect_x_get, _cv.CvRect_x_set)
    __swig_setmethods__["y"] = _cv.CvRect_y_set
    __swig_getmethods__["y"] = _cv.CvRect_y_get
    if _newclass:y = _swig_property(_cv.CvRect_y_get, _cv.CvRect_y_set)
    __swig_setmethods__["width"] = _cv.CvRect_width_set
    __swig_getmethods__["width"] = _cv.CvRect_width_get
    if _newclass:width = _swig_property(_cv.CvRect_width_get, _cv.CvRect_width_set)
    __swig_setmethods__["height"] = _cv.CvRect_height_set
    __swig_getmethods__["height"] = _cv.CvRect_height_get
    if _newclass:height = _swig_property(_cv.CvRect_height_get, _cv.CvRect_height_set)
    def __init__(self, *args): 
        """__init__(self) -> CvRect"""
        this = _cv.new_CvRect(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvRect
    __del__ = lambda self : None;
CvRect_swigregister = _cv.CvRect_swigregister
CvRect_swigregister(CvRect)


def cvRect(*args):
  """cvRect(int x, int y, int width, int height) -> CvRect"""
  return _cv.cvRect(*args)

def cvRectToROI(*args):
  """cvRectToROI(CvRect rect, int coi)"""
  return _cv.cvRectToROI(*args)

def cvROIToRect(*args):
  """cvROIToRect( roi) -> CvRect"""
  return _cv.cvROIToRect(*args)
class CvTermCriteria(_object):
    """Proxy of C++ CvTermCriteria class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvTermCriteria, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvTermCriteria, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _cv.CvTermCriteria_type_set
    __swig_getmethods__["type"] = _cv.CvTermCriteria_type_get
    if _newclass:type = _swig_property(_cv.CvTermCriteria_type_get, _cv.CvTermCriteria_type_set)
    __swig_setmethods__["max_iter"] = _cv.CvTermCriteria_max_iter_set
    __swig_getmethods__["max_iter"] = _cv.CvTermCriteria_max_iter_get
    if _newclass:max_iter = _swig_property(_cv.CvTermCriteria_max_iter_get, _cv.CvTermCriteria_max_iter_set)
    __swig_setmethods__["epsilon"] = _cv.CvTermCriteria_epsilon_set
    __swig_getmethods__["epsilon"] = _cv.CvTermCriteria_epsilon_get
    if _newclass:epsilon = _swig_property(_cv.CvTermCriteria_epsilon_get, _cv.CvTermCriteria_epsilon_set)
    def __init__(self, *args): 
        """__init__(self) -> CvTermCriteria"""
        this = _cv.new_CvTermCriteria(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvTermCriteria
    __del__ = lambda self : None;
CvTermCriteria_swigregister = _cv.CvTermCriteria_swigregister
CvTermCriteria_swigregister(CvTermCriteria)


def cvTermCriteria(*args):
  """cvTermCriteria(int type, int max_iter, double epsilon) -> CvTermCriteria"""
  return _cv.cvTermCriteria(*args)
class CvPoint(_object):
    """Proxy of C++ CvPoint class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvPoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvPoint, name)
    __swig_setmethods__["x"] = _cv.CvPoint_x_set
    __swig_getmethods__["x"] = _cv.CvPoint_x_get
    if _newclass:x = _swig_property(_cv.CvPoint_x_get, _cv.CvPoint_x_set)
    __swig_setmethods__["y"] = _cv.CvPoint_y_set
    __swig_getmethods__["y"] = _cv.CvPoint_y_get
    if _newclass:y = _swig_property(_cv.CvPoint_y_get, _cv.CvPoint_y_set)
    def __str__(*args):
        """__str__(self) -> char"""
        return _cv.CvPoint___str__(*args)

    def __repr__(*args):
        """__repr__(self) -> char"""
        return _cv.CvPoint___repr__(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvPoint"""
        this = _cv.new_CvPoint(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvPoint
    __del__ = lambda self : None;
CvPoint_swigregister = _cv.CvPoint_swigregister
CvPoint_swigregister(CvPoint)


def cvPoint(*args):
  """cvPoint(int x, int y) -> CvPoint"""
  return _cv.cvPoint(*args)
class CvPoint2D32f(_object):
    """Proxy of C++ CvPoint2D32f class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvPoint2D32f, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvPoint2D32f, name)
    __swig_setmethods__["x"] = _cv.CvPoint2D32f_x_set
    __swig_getmethods__["x"] = _cv.CvPoint2D32f_x_get
    if _newclass:x = _swig_property(_cv.CvPoint2D32f_x_get, _cv.CvPoint2D32f_x_set)
    __swig_setmethods__["y"] = _cv.CvPoint2D32f_y_set
    __swig_getmethods__["y"] = _cv.CvPoint2D32f_y_get
    if _newclass:y = _swig_property(_cv.CvPoint2D32f_y_get, _cv.CvPoint2D32f_y_set)
    def __str__(*args):
        """__str__(self) -> char"""
        return _cv.CvPoint2D32f___str__(*args)

    def __repr__(*args):
        """__repr__(self) -> char"""
        return _cv.CvPoint2D32f___repr__(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvPoint2D32f"""
        this = _cv.new_CvPoint2D32f(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvPoint2D32f
    __del__ = lambda self : None;
CvPoint2D32f_swigregister = _cv.CvPoint2D32f_swigregister
CvPoint2D32f_swigregister(CvPoint2D32f)


def cvPoint2D32f(*args):
  """cvPoint2D32f(double x, double y) -> CvPoint2D32f"""
  return _cv.cvPoint2D32f(*args)

def cvPointTo32f(*args):
  """cvPointTo32f(CvPoint point) -> CvPoint2D32f"""
  return _cv.cvPointTo32f(*args)

def cvPointFrom32f(*args):
  """cvPointFrom32f(CvPoint2D32f point) -> CvPoint"""
  return _cv.cvPointFrom32f(*args)
class CvPoint3D32f(_object):
    """Proxy of C++ CvPoint3D32f class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvPoint3D32f, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvPoint3D32f, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _cv.CvPoint3D32f_x_set
    __swig_getmethods__["x"] = _cv.CvPoint3D32f_x_get
    if _newclass:x = _swig_property(_cv.CvPoint3D32f_x_get, _cv.CvPoint3D32f_x_set)
    __swig_setmethods__["y"] = _cv.CvPoint3D32f_y_set
    __swig_getmethods__["y"] = _cv.CvPoint3D32f_y_get
    if _newclass:y = _swig_property(_cv.CvPoint3D32f_y_get, _cv.CvPoint3D32f_y_set)
    __swig_setmethods__["z"] = _cv.CvPoint3D32f_z_set
    __swig_getmethods__["z"] = _cv.CvPoint3D32f_z_get
    if _newclass:z = _swig_property(_cv.CvPoint3D32f_z_get, _cv.CvPoint3D32f_z_set)
    def __init__(self, *args): 
        """__init__(self) -> CvPoint3D32f"""
        this = _cv.new_CvPoint3D32f(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvPoint3D32f
    __del__ = lambda self : None;
CvPoint3D32f_swigregister = _cv.CvPoint3D32f_swigregister
CvPoint3D32f_swigregister(CvPoint3D32f)


def cvPoint3D32f(*args):
  """cvPoint3D32f(double x, double y, double z) -> CvPoint3D32f"""
  return _cv.cvPoint3D32f(*args)
class CvPoint2D64f(_object):
    """Proxy of C++ CvPoint2D64f class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvPoint2D64f, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvPoint2D64f, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _cv.CvPoint2D64f_x_set
    __swig_getmethods__["x"] = _cv.CvPoint2D64f_x_get
    if _newclass:x = _swig_property(_cv.CvPoint2D64f_x_get, _cv.CvPoint2D64f_x_set)
    __swig_setmethods__["y"] = _cv.CvPoint2D64f_y_set
    __swig_getmethods__["y"] = _cv.CvPoint2D64f_y_get
    if _newclass:y = _swig_property(_cv.CvPoint2D64f_y_get, _cv.CvPoint2D64f_y_set)
    def __init__(self, *args): 
        """__init__(self) -> CvPoint2D64f"""
        this = _cv.new_CvPoint2D64f(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvPoint2D64f
    __del__ = lambda self : None;
CvPoint2D64f_swigregister = _cv.CvPoint2D64f_swigregister
CvPoint2D64f_swigregister(CvPoint2D64f)


def cvPoint2D64f(*args):
  """cvPoint2D64f(double x, double y) -> CvPoint2D64f"""
  return _cv.cvPoint2D64f(*args)
class CvPoint3D64f(_object):
    """Proxy of C++ CvPoint3D64f class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvPoint3D64f, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvPoint3D64f, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _cv.CvPoint3D64f_x_set
    __swig_getmethods__["x"] = _cv.CvPoint3D64f_x_get
    if _newclass:x = _swig_property(_cv.CvPoint3D64f_x_get, _cv.CvPoint3D64f_x_set)
    __swig_setmethods__["y"] = _cv.CvPoint3D64f_y_set
    __swig_getmethods__["y"] = _cv.CvPoint3D64f_y_get
    if _newclass:y = _swig_property(_cv.CvPoint3D64f_y_get, _cv.CvPoint3D64f_y_set)
    __swig_setmethods__["z"] = _cv.CvPoint3D64f_z_set
    __swig_getmethods__["z"] = _cv.CvPoint3D64f_z_get
    if _newclass:z = _swig_property(_cv.CvPoint3D64f_z_get, _cv.CvPoint3D64f_z_set)
    def __init__(self, *args): 
        """__init__(self) -> CvPoint3D64f"""
        this = _cv.new_CvPoint3D64f(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvPoint3D64f
    __del__ = lambda self : None;
CvPoint3D64f_swigregister = _cv.CvPoint3D64f_swigregister
CvPoint3D64f_swigregister(CvPoint3D64f)


def cvPoint3D64f(*args):
  """cvPoint3D64f(double x, double y, double z) -> CvPoint3D64f"""
  return _cv.cvPoint3D64f(*args)
class CvSize(_object):
    """Proxy of C++ CvSize class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSize, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSize, name)
    __repr__ = _swig_repr
    __swig_setmethods__["width"] = _cv.CvSize_width_set
    __swig_getmethods__["width"] = _cv.CvSize_width_get
    if _newclass:width = _swig_property(_cv.CvSize_width_get, _cv.CvSize_width_set)
    __swig_setmethods__["height"] = _cv.CvSize_height_set
    __swig_getmethods__["height"] = _cv.CvSize_height_get
    if _newclass:height = _swig_property(_cv.CvSize_height_get, _cv.CvSize_height_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSize"""
        this = _cv.new_CvSize(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSize
    __del__ = lambda self : None;
CvSize_swigregister = _cv.CvSize_swigregister
CvSize_swigregister(CvSize)


def cvSize(*args):
  """cvSize(int width, int height) -> CvSize"""
  return _cv.cvSize(*args)
class CvSize2D32f(_object):
    """Proxy of C++ CvSize2D32f class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSize2D32f, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSize2D32f, name)
    __repr__ = _swig_repr
    __swig_setmethods__["width"] = _cv.CvSize2D32f_width_set
    __swig_getmethods__["width"] = _cv.CvSize2D32f_width_get
    if _newclass:width = _swig_property(_cv.CvSize2D32f_width_get, _cv.CvSize2D32f_width_set)
    __swig_setmethods__["height"] = _cv.CvSize2D32f_height_set
    __swig_getmethods__["height"] = _cv.CvSize2D32f_height_get
    if _newclass:height = _swig_property(_cv.CvSize2D32f_height_get, _cv.CvSize2D32f_height_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSize2D32f"""
        this = _cv.new_CvSize2D32f(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSize2D32f
    __del__ = lambda self : None;
CvSize2D32f_swigregister = _cv.CvSize2D32f_swigregister
CvSize2D32f_swigregister(CvSize2D32f)


def cvSize2D32f(*args):
  """cvSize2D32f(double width, double height) -> CvSize2D32f"""
  return _cv.cvSize2D32f(*args)
class CvBox2D(_object):
    """Proxy of C++ CvBox2D class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvBox2D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvBox2D, name)
    __repr__ = _swig_repr
    __swig_setmethods__["center"] = _cv.CvBox2D_center_set
    __swig_getmethods__["center"] = _cv.CvBox2D_center_get
    if _newclass:center = _swig_property(_cv.CvBox2D_center_get, _cv.CvBox2D_center_set)
    __swig_setmethods__["size"] = _cv.CvBox2D_size_set
    __swig_getmethods__["size"] = _cv.CvBox2D_size_get
    if _newclass:size = _swig_property(_cv.CvBox2D_size_get, _cv.CvBox2D_size_set)
    __swig_setmethods__["angle"] = _cv.CvBox2D_angle_set
    __swig_getmethods__["angle"] = _cv.CvBox2D_angle_get
    if _newclass:angle = _swig_property(_cv.CvBox2D_angle_get, _cv.CvBox2D_angle_set)
    def __init__(self, *args): 
        """__init__(self) -> CvBox2D"""
        this = _cv.new_CvBox2D(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvBox2D
    __del__ = lambda self : None;
CvBox2D_swigregister = _cv.CvBox2D_swigregister
CvBox2D_swigregister(CvBox2D)

class CvLineIterator(_object):
    """Proxy of C++ CvLineIterator class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvLineIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvLineIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ptr"] = _cv.CvLineIterator_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvLineIterator_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvLineIterator_ptr_get, _cv.CvLineIterator_ptr_set)
    __swig_setmethods__["err"] = _cv.CvLineIterator_err_set
    __swig_getmethods__["err"] = _cv.CvLineIterator_err_get
    if _newclass:err = _swig_property(_cv.CvLineIterator_err_get, _cv.CvLineIterator_err_set)
    __swig_setmethods__["plus_delta"] = _cv.CvLineIterator_plus_delta_set
    __swig_getmethods__["plus_delta"] = _cv.CvLineIterator_plus_delta_get
    if _newclass:plus_delta = _swig_property(_cv.CvLineIterator_plus_delta_get, _cv.CvLineIterator_plus_delta_set)
    __swig_setmethods__["minus_delta"] = _cv.CvLineIterator_minus_delta_set
    __swig_getmethods__["minus_delta"] = _cv.CvLineIterator_minus_delta_get
    if _newclass:minus_delta = _swig_property(_cv.CvLineIterator_minus_delta_get, _cv.CvLineIterator_minus_delta_set)
    __swig_setmethods__["plus_step"] = _cv.CvLineIterator_plus_step_set
    __swig_getmethods__["plus_step"] = _cv.CvLineIterator_plus_step_get
    if _newclass:plus_step = _swig_property(_cv.CvLineIterator_plus_step_get, _cv.CvLineIterator_plus_step_set)
    __swig_setmethods__["minus_step"] = _cv.CvLineIterator_minus_step_set
    __swig_getmethods__["minus_step"] = _cv.CvLineIterator_minus_step_get
    if _newclass:minus_step = _swig_property(_cv.CvLineIterator_minus_step_get, _cv.CvLineIterator_minus_step_set)
    def __init__(self, *args): 
        """__init__(self) -> CvLineIterator"""
        this = _cv.new_CvLineIterator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvLineIterator
    __del__ = lambda self : None;
CvLineIterator_swigregister = _cv.CvLineIterator_swigregister
CvLineIterator_swigregister(CvLineIterator)

class CvSlice(_object):
    """Proxy of C++ CvSlice class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSlice, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSlice, name)
    __repr__ = _swig_repr
    __swig_setmethods__["start_index"] = _cv.CvSlice_start_index_set
    __swig_getmethods__["start_index"] = _cv.CvSlice_start_index_get
    if _newclass:start_index = _swig_property(_cv.CvSlice_start_index_get, _cv.CvSlice_start_index_set)
    __swig_setmethods__["end_index"] = _cv.CvSlice_end_index_set
    __swig_getmethods__["end_index"] = _cv.CvSlice_end_index_get
    if _newclass:end_index = _swig_property(_cv.CvSlice_end_index_get, _cv.CvSlice_end_index_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSlice"""
        this = _cv.new_CvSlice(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSlice
    __del__ = lambda self : None;
CvSlice_swigregister = _cv.CvSlice_swigregister
CvSlice_swigregister(CvSlice)


def cvSlice(*args):
  """cvSlice(int start, int end) -> CvSlice"""
  return _cv.cvSlice(*args)
class CvScalar(_object):
    """Proxy of C++ CvScalar class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvScalar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvScalar, name)
    __swig_setmethods__["val"] = _cv.CvScalar_val_set
    __swig_getmethods__["val"] = _cv.CvScalar_val_get
    if _newclass:val = _swig_property(_cv.CvScalar_val_get, _cv.CvScalar_val_set)
    def __str__(*args):
        """__str__(self) -> char"""
        return _cv.CvScalar___str__(*args)

    def __repr__(*args):
        """__repr__(self) -> char"""
        return _cv.CvScalar___repr__(*args)

    def __getitem__(*args):
        """__getitem__(self, int index) -> double"""
        return _cv.CvScalar___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int index, double value)"""
        return _cv.CvScalar___setitem__(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvScalar"""
        this = _cv.new_CvScalar(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvScalar
    __del__ = lambda self : None;
CvScalar_swigregister = _cv.CvScalar_swigregister
CvScalar_swigregister(CvScalar)


def cvRealScalar(*args):
  """cvRealScalar(double val0) -> CvScalar"""
  return _cv.cvRealScalar(*args)

def cvScalarAll(*args):
  """cvScalarAll(double val0123) -> CvScalar"""
  return _cv.cvScalarAll(*args)
class CvMemBlock(_object):
    """Proxy of C++ CvMemBlock class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMemBlock, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMemBlock, name)
    __repr__ = _swig_repr
    __swig_setmethods__["prev"] = _cv.CvMemBlock_prev_set
    __swig_getmethods__["prev"] = _cv.CvMemBlock_prev_get
    if _newclass:prev = _swig_property(_cv.CvMemBlock_prev_get, _cv.CvMemBlock_prev_set)
    __swig_setmethods__["next"] = _cv.CvMemBlock_next_set
    __swig_getmethods__["next"] = _cv.CvMemBlock_next_get
    if _newclass:next = _swig_property(_cv.CvMemBlock_next_get, _cv.CvMemBlock_next_set)
    def __init__(self, *args): 
        """__init__(self) -> CvMemBlock"""
        this = _cv.new_CvMemBlock(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMemBlock
    __del__ = lambda self : None;
CvMemBlock_swigregister = _cv.CvMemBlock_swigregister
CvMemBlock_swigregister(CvMemBlock)

def cvScalar(*args):
  """
    cvScalar(double val0, double val1=0, double val2=0, double val3=0) -> CvScalar
    cvScalar(double val0, double val1=0, double val2=0) -> CvScalar
    cvScalar(double val0, double val1=0) -> CvScalar
    cvScalar(double val0) -> CvScalar
    """
  return _cv.cvScalar(*args)

class CvMemStorage(_object):
    """Proxy of C++ CvMemStorage class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMemStorage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMemStorage, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["signature"] = _cv.CvMemStorage_signature_set
    __swig_getmethods__["signature"] = _cv.CvMemStorage_signature_get
    if _newclass:signature = _swig_property(_cv.CvMemStorage_signature_get, _cv.CvMemStorage_signature_set)
    __swig_setmethods__["bottom"] = _cv.CvMemStorage_bottom_set
    __swig_getmethods__["bottom"] = _cv.CvMemStorage_bottom_get
    if _newclass:bottom = _swig_property(_cv.CvMemStorage_bottom_get, _cv.CvMemStorage_bottom_set)
    __swig_setmethods__["top"] = _cv.CvMemStorage_top_set
    __swig_getmethods__["top"] = _cv.CvMemStorage_top_get
    if _newclass:top = _swig_property(_cv.CvMemStorage_top_get, _cv.CvMemStorage_top_set)
    __swig_setmethods__["parent"] = _cv.CvMemStorage_parent_set
    __swig_getmethods__["parent"] = _cv.CvMemStorage_parent_get
    if _newclass:parent = _swig_property(_cv.CvMemStorage_parent_get, _cv.CvMemStorage_parent_set)
    __swig_setmethods__["block_size"] = _cv.CvMemStorage_block_size_set
    __swig_getmethods__["block_size"] = _cv.CvMemStorage_block_size_get
    if _newclass:block_size = _swig_property(_cv.CvMemStorage_block_size_get, _cv.CvMemStorage_block_size_set)
    __swig_setmethods__["free_space"] = _cv.CvMemStorage_free_space_set
    __swig_getmethods__["free_space"] = _cv.CvMemStorage_free_space_get
    if _newclass:free_space = _swig_property(_cv.CvMemStorage_free_space_get, _cv.CvMemStorage_free_space_set)
    __swig_destroy__ = _cv.delete_CvMemStorage
    __del__ = lambda self : None;
CvMemStorage_swigregister = _cv.CvMemStorage_swigregister
CvMemStorage_swigregister(CvMemStorage)

class CvMemStoragePos(_object):
    """Proxy of C++ CvMemStoragePos class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMemStoragePos, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMemStoragePos, name)
    __repr__ = _swig_repr
    __swig_setmethods__["top"] = _cv.CvMemStoragePos_top_set
    __swig_getmethods__["top"] = _cv.CvMemStoragePos_top_get
    if _newclass:top = _swig_property(_cv.CvMemStoragePos_top_get, _cv.CvMemStoragePos_top_set)
    __swig_setmethods__["free_space"] = _cv.CvMemStoragePos_free_space_set
    __swig_getmethods__["free_space"] = _cv.CvMemStoragePos_free_space_get
    if _newclass:free_space = _swig_property(_cv.CvMemStoragePos_free_space_get, _cv.CvMemStoragePos_free_space_set)
    def __init__(self, *args): 
        """__init__(self) -> CvMemStoragePos"""
        this = _cv.new_CvMemStoragePos(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMemStoragePos
    __del__ = lambda self : None;
CvMemStoragePos_swigregister = _cv.CvMemStoragePos_swigregister
CvMemStoragePos_swigregister(CvMemStoragePos)

class CvSeqBlock(_object):
    """Proxy of C++ CvSeqBlock class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeqBlock, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeqBlock, name)
    __repr__ = _swig_repr
    __swig_setmethods__["prev"] = _cv.CvSeqBlock_prev_set
    __swig_getmethods__["prev"] = _cv.CvSeqBlock_prev_get
    if _newclass:prev = _swig_property(_cv.CvSeqBlock_prev_get, _cv.CvSeqBlock_prev_set)
    __swig_setmethods__["next"] = _cv.CvSeqBlock_next_set
    __swig_getmethods__["next"] = _cv.CvSeqBlock_next_get
    if _newclass:next = _swig_property(_cv.CvSeqBlock_next_get, _cv.CvSeqBlock_next_set)
    __swig_setmethods__["start_index"] = _cv.CvSeqBlock_start_index_set
    __swig_getmethods__["start_index"] = _cv.CvSeqBlock_start_index_get
    if _newclass:start_index = _swig_property(_cv.CvSeqBlock_start_index_get, _cv.CvSeqBlock_start_index_set)
    __swig_setmethods__["count"] = _cv.CvSeqBlock_count_set
    __swig_getmethods__["count"] = _cv.CvSeqBlock_count_get
    if _newclass:count = _swig_property(_cv.CvSeqBlock_count_get, _cv.CvSeqBlock_count_set)
    __swig_setmethods__["data"] = _cv.CvSeqBlock_data_set
    __swig_getmethods__["data"] = _cv.CvSeqBlock_data_get
    if _newclass:data = _swig_property(_cv.CvSeqBlock_data_get, _cv.CvSeqBlock_data_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSeqBlock"""
        this = _cv.new_CvSeqBlock(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeqBlock
    __del__ = lambda self : None;
CvSeqBlock_swigregister = _cv.CvSeqBlock_swigregister
CvSeqBlock_swigregister(CvSeqBlock)

class CvSeq(_object):
    """Proxy of C++ CvSeq class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvSeq_flags_set
    __swig_getmethods__["flags"] = _cv.CvSeq_flags_get
    if _newclass:flags = _swig_property(_cv.CvSeq_flags_get, _cv.CvSeq_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvSeq_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvSeq_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvSeq_header_size_get, _cv.CvSeq_header_size_set)
    __swig_setmethods__["h_prev"] = _cv.CvSeq_h_prev_set
    __swig_getmethods__["h_prev"] = _cv.CvSeq_h_prev_get
    if _newclass:h_prev = _swig_property(_cv.CvSeq_h_prev_get, _cv.CvSeq_h_prev_set)
    __swig_setmethods__["h_next"] = _cv.CvSeq_h_next_set
    __swig_getmethods__["h_next"] = _cv.CvSeq_h_next_get
    if _newclass:h_next = _swig_property(_cv.CvSeq_h_next_get, _cv.CvSeq_h_next_set)
    __swig_setmethods__["v_prev"] = _cv.CvSeq_v_prev_set
    __swig_getmethods__["v_prev"] = _cv.CvSeq_v_prev_get
    if _newclass:v_prev = _swig_property(_cv.CvSeq_v_prev_get, _cv.CvSeq_v_prev_set)
    __swig_setmethods__["v_next"] = _cv.CvSeq_v_next_set
    __swig_getmethods__["v_next"] = _cv.CvSeq_v_next_get
    if _newclass:v_next = _swig_property(_cv.CvSeq_v_next_get, _cv.CvSeq_v_next_set)
    __swig_setmethods__["total"] = _cv.CvSeq_total_set
    __swig_getmethods__["total"] = _cv.CvSeq_total_get
    if _newclass:total = _swig_property(_cv.CvSeq_total_get, _cv.CvSeq_total_set)
    __swig_setmethods__["elem_size"] = _cv.CvSeq_elem_size_set
    __swig_getmethods__["elem_size"] = _cv.CvSeq_elem_size_get
    if _newclass:elem_size = _swig_property(_cv.CvSeq_elem_size_get, _cv.CvSeq_elem_size_set)
    __swig_setmethods__["block_max"] = _cv.CvSeq_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvSeq_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvSeq_block_max_get, _cv.CvSeq_block_max_set)
    __swig_setmethods__["ptr"] = _cv.CvSeq_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvSeq_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvSeq_ptr_get, _cv.CvSeq_ptr_set)
    __swig_setmethods__["delta_elems"] = _cv.CvSeq_delta_elems_set
    __swig_getmethods__["delta_elems"] = _cv.CvSeq_delta_elems_get
    if _newclass:delta_elems = _swig_property(_cv.CvSeq_delta_elems_get, _cv.CvSeq_delta_elems_set)
    __swig_setmethods__["storage"] = _cv.CvSeq_storage_set
    __swig_getmethods__["storage"] = _cv.CvSeq_storage_get
    if _newclass:storage = _swig_property(_cv.CvSeq_storage_get, _cv.CvSeq_storage_set)
    __swig_setmethods__["free_blocks"] = _cv.CvSeq_free_blocks_set
    __swig_getmethods__["free_blocks"] = _cv.CvSeq_free_blocks_get
    if _newclass:free_blocks = _swig_property(_cv.CvSeq_free_blocks_get, _cv.CvSeq_free_blocks_set)
    __swig_setmethods__["first"] = _cv.CvSeq_first_set
    __swig_getmethods__["first"] = _cv.CvSeq_first_get
    if _newclass:first = _swig_property(_cv.CvSeq_first_get, _cv.CvSeq_first_set)
    def __iter__(self):
    	"""
    	generator function iterating elements in the sequence
    	"""
    	for i in range(self.total):
    		yield self[i]

    def vrange(self):
    	"""
    	generator function iterating along v_next
    	"""
    	s = self
    	t = type(self)
    	while s:
    		yield s
    		s = t.cast(s.v_next)

    def hrange(self):
    	"""
    	generator function iterating along h_next
    	"""
    	s = self
    	t = type(self)
    	while s:
    		yield s
    		s = t.cast(s.h_next)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq"""
        this = _cv.new_CvSeq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq
    __del__ = lambda self : None;
CvSeq_swigregister = _cv.CvSeq_swigregister
CvSeq_swigregister(CvSeq)

class CvSetElem(_object):
    """Proxy of C++ CvSetElem class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSetElem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSetElem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvSetElem_flags_set
    __swig_getmethods__["flags"] = _cv.CvSetElem_flags_get
    if _newclass:flags = _swig_property(_cv.CvSetElem_flags_get, _cv.CvSetElem_flags_set)
    __swig_setmethods__["next_free"] = _cv.CvSetElem_next_free_set
    __swig_getmethods__["next_free"] = _cv.CvSetElem_next_free_get
    if _newclass:next_free = _swig_property(_cv.CvSetElem_next_free_get, _cv.CvSetElem_next_free_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSetElem"""
        this = _cv.new_CvSetElem(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSetElem
    __del__ = lambda self : None;
CvSetElem_swigregister = _cv.CvSetElem_swigregister
CvSetElem_swigregister(CvSetElem)

class CvSet(_object):
    """Proxy of C++ CvSet class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSet, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvSet_flags_set
    __swig_getmethods__["flags"] = _cv.CvSet_flags_get
    if _newclass:flags = _swig_property(_cv.CvSet_flags_get, _cv.CvSet_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvSet_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvSet_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvSet_header_size_get, _cv.CvSet_header_size_set)
    __swig_setmethods__["h_prev"] = _cv.CvSet_h_prev_set
    __swig_getmethods__["h_prev"] = _cv.CvSet_h_prev_get
    if _newclass:h_prev = _swig_property(_cv.CvSet_h_prev_get, _cv.CvSet_h_prev_set)
    __swig_setmethods__["h_next"] = _cv.CvSet_h_next_set
    __swig_getmethods__["h_next"] = _cv.CvSet_h_next_get
    if _newclass:h_next = _swig_property(_cv.CvSet_h_next_get, _cv.CvSet_h_next_set)
    __swig_setmethods__["v_prev"] = _cv.CvSet_v_prev_set
    __swig_getmethods__["v_prev"] = _cv.CvSet_v_prev_get
    if _newclass:v_prev = _swig_property(_cv.CvSet_v_prev_get, _cv.CvSet_v_prev_set)
    __swig_setmethods__["v_next"] = _cv.CvSet_v_next_set
    __swig_getmethods__["v_next"] = _cv.CvSet_v_next_get
    if _newclass:v_next = _swig_property(_cv.CvSet_v_next_get, _cv.CvSet_v_next_set)
    __swig_setmethods__["total"] = _cv.CvSet_total_set
    __swig_getmethods__["total"] = _cv.CvSet_total_get
    if _newclass:total = _swig_property(_cv.CvSet_total_get, _cv.CvSet_total_set)
    __swig_setmethods__["elem_size"] = _cv.CvSet_elem_size_set
    __swig_getmethods__["elem_size"] = _cv.CvSet_elem_size_get
    if _newclass:elem_size = _swig_property(_cv.CvSet_elem_size_get, _cv.CvSet_elem_size_set)
    __swig_setmethods__["block_max"] = _cv.CvSet_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvSet_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvSet_block_max_get, _cv.CvSet_block_max_set)
    __swig_setmethods__["ptr"] = _cv.CvSet_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvSet_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvSet_ptr_get, _cv.CvSet_ptr_set)
    __swig_setmethods__["delta_elems"] = _cv.CvSet_delta_elems_set
    __swig_getmethods__["delta_elems"] = _cv.CvSet_delta_elems_get
    if _newclass:delta_elems = _swig_property(_cv.CvSet_delta_elems_get, _cv.CvSet_delta_elems_set)
    __swig_setmethods__["storage"] = _cv.CvSet_storage_set
    __swig_getmethods__["storage"] = _cv.CvSet_storage_get
    if _newclass:storage = _swig_property(_cv.CvSet_storage_get, _cv.CvSet_storage_set)
    __swig_setmethods__["free_blocks"] = _cv.CvSet_free_blocks_set
    __swig_getmethods__["free_blocks"] = _cv.CvSet_free_blocks_get
    if _newclass:free_blocks = _swig_property(_cv.CvSet_free_blocks_get, _cv.CvSet_free_blocks_set)
    __swig_setmethods__["first"] = _cv.CvSet_first_set
    __swig_getmethods__["first"] = _cv.CvSet_first_get
    if _newclass:first = _swig_property(_cv.CvSet_first_get, _cv.CvSet_first_set)
    __swig_setmethods__["free_elems"] = _cv.CvSet_free_elems_set
    __swig_getmethods__["free_elems"] = _cv.CvSet_free_elems_get
    if _newclass:free_elems = _swig_property(_cv.CvSet_free_elems_get, _cv.CvSet_free_elems_set)
    __swig_setmethods__["active_count"] = _cv.CvSet_active_count_set
    __swig_getmethods__["active_count"] = _cv.CvSet_active_count_get
    if _newclass:active_count = _swig_property(_cv.CvSet_active_count_get, _cv.CvSet_active_count_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSet"""
        this = _cv.new_CvSet(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSet
    __del__ = lambda self : None;
CvSet_swigregister = _cv.CvSet_swigregister
CvSet_swigregister(CvSet)

class CvGraphEdge(_object):
    """Proxy of C++ CvGraphEdge class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvGraphEdge, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvGraphEdge, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvGraphEdge_flags_set
    __swig_getmethods__["flags"] = _cv.CvGraphEdge_flags_get
    if _newclass:flags = _swig_property(_cv.CvGraphEdge_flags_get, _cv.CvGraphEdge_flags_set)
    __swig_setmethods__["weight"] = _cv.CvGraphEdge_weight_set
    __swig_getmethods__["weight"] = _cv.CvGraphEdge_weight_get
    if _newclass:weight = _swig_property(_cv.CvGraphEdge_weight_get, _cv.CvGraphEdge_weight_set)
    __swig_setmethods__["next"] = _cv.CvGraphEdge_next_set
    __swig_getmethods__["next"] = _cv.CvGraphEdge_next_get
    if _newclass:next = _swig_property(_cv.CvGraphEdge_next_get, _cv.CvGraphEdge_next_set)
    __swig_setmethods__["vtx"] = _cv.CvGraphEdge_vtx_set
    __swig_getmethods__["vtx"] = _cv.CvGraphEdge_vtx_get
    if _newclass:vtx = _swig_property(_cv.CvGraphEdge_vtx_get, _cv.CvGraphEdge_vtx_set)
    def __init__(self, *args): 
        """__init__(self) -> CvGraphEdge"""
        this = _cv.new_CvGraphEdge(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvGraphEdge
    __del__ = lambda self : None;
CvGraphEdge_swigregister = _cv.CvGraphEdge_swigregister
CvGraphEdge_swigregister(CvGraphEdge)

class CvGraphVtx(_object):
    """Proxy of C++ CvGraphVtx class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvGraphVtx, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvGraphVtx, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvGraphVtx_flags_set
    __swig_getmethods__["flags"] = _cv.CvGraphVtx_flags_get
    if _newclass:flags = _swig_property(_cv.CvGraphVtx_flags_get, _cv.CvGraphVtx_flags_set)
    __swig_setmethods__["first"] = _cv.CvGraphVtx_first_set
    __swig_getmethods__["first"] = _cv.CvGraphVtx_first_get
    if _newclass:first = _swig_property(_cv.CvGraphVtx_first_get, _cv.CvGraphVtx_first_set)
    def __init__(self, *args): 
        """__init__(self) -> CvGraphVtx"""
        this = _cv.new_CvGraphVtx(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvGraphVtx
    __del__ = lambda self : None;
CvGraphVtx_swigregister = _cv.CvGraphVtx_swigregister
CvGraphVtx_swigregister(CvGraphVtx)

class CvGraphVtx2D(_object):
    """Proxy of C++ CvGraphVtx2D class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvGraphVtx2D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvGraphVtx2D, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvGraphVtx2D_flags_set
    __swig_getmethods__["flags"] = _cv.CvGraphVtx2D_flags_get
    if _newclass:flags = _swig_property(_cv.CvGraphVtx2D_flags_get, _cv.CvGraphVtx2D_flags_set)
    __swig_setmethods__["first"] = _cv.CvGraphVtx2D_first_set
    __swig_getmethods__["first"] = _cv.CvGraphVtx2D_first_get
    if _newclass:first = _swig_property(_cv.CvGraphVtx2D_first_get, _cv.CvGraphVtx2D_first_set)
    __swig_setmethods__["ptr"] = _cv.CvGraphVtx2D_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvGraphVtx2D_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvGraphVtx2D_ptr_get, _cv.CvGraphVtx2D_ptr_set)
    def __init__(self, *args): 
        """__init__(self) -> CvGraphVtx2D"""
        this = _cv.new_CvGraphVtx2D(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvGraphVtx2D
    __del__ = lambda self : None;
CvGraphVtx2D_swigregister = _cv.CvGraphVtx2D_swigregister
CvGraphVtx2D_swigregister(CvGraphVtx2D)

class CvGraph(_object):
    """Proxy of C++ CvGraph class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvGraph, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvGraph, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvGraph_flags_set
    __swig_getmethods__["flags"] = _cv.CvGraph_flags_get
    if _newclass:flags = _swig_property(_cv.CvGraph_flags_get, _cv.CvGraph_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvGraph_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvGraph_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvGraph_header_size_get, _cv.CvGraph_header_size_set)
    __swig_setmethods__["h_prev"] = _cv.CvGraph_h_prev_set
    __swig_getmethods__["h_prev"] = _cv.CvGraph_h_prev_get
    if _newclass:h_prev = _swig_property(_cv.CvGraph_h_prev_get, _cv.CvGraph_h_prev_set)
    __swig_setmethods__["h_next"] = _cv.CvGraph_h_next_set
    __swig_getmethods__["h_next"] = _cv.CvGraph_h_next_get
    if _newclass:h_next = _swig_property(_cv.CvGraph_h_next_get, _cv.CvGraph_h_next_set)
    __swig_setmethods__["v_prev"] = _cv.CvGraph_v_prev_set
    __swig_getmethods__["v_prev"] = _cv.CvGraph_v_prev_get
    if _newclass:v_prev = _swig_property(_cv.CvGraph_v_prev_get, _cv.CvGraph_v_prev_set)
    __swig_setmethods__["v_next"] = _cv.CvGraph_v_next_set
    __swig_getmethods__["v_next"] = _cv.CvGraph_v_next_get
    if _newclass:v_next = _swig_property(_cv.CvGraph_v_next_get, _cv.CvGraph_v_next_set)
    __swig_setmethods__["total"] = _cv.CvGraph_total_set
    __swig_getmethods__["total"] = _cv.CvGraph_total_get
    if _newclass:total = _swig_property(_cv.CvGraph_total_get, _cv.CvGraph_total_set)
    __swig_setmethods__["elem_size"] = _cv.CvGraph_elem_size_set
    __swig_getmethods__["elem_size"] = _cv.CvGraph_elem_size_get
    if _newclass:elem_size = _swig_property(_cv.CvGraph_elem_size_get, _cv.CvGraph_elem_size_set)
    __swig_setmethods__["block_max"] = _cv.CvGraph_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvGraph_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvGraph_block_max_get, _cv.CvGraph_block_max_set)
    __swig_setmethods__["ptr"] = _cv.CvGraph_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvGraph_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvGraph_ptr_get, _cv.CvGraph_ptr_set)
    __swig_setmethods__["delta_elems"] = _cv.CvGraph_delta_elems_set
    __swig_getmethods__["delta_elems"] = _cv.CvGraph_delta_elems_get
    if _newclass:delta_elems = _swig_property(_cv.CvGraph_delta_elems_get, _cv.CvGraph_delta_elems_set)
    __swig_setmethods__["storage"] = _cv.CvGraph_storage_set
    __swig_getmethods__["storage"] = _cv.CvGraph_storage_get
    if _newclass:storage = _swig_property(_cv.CvGraph_storage_get, _cv.CvGraph_storage_set)
    __swig_setmethods__["free_blocks"] = _cv.CvGraph_free_blocks_set
    __swig_getmethods__["free_blocks"] = _cv.CvGraph_free_blocks_get
    if _newclass:free_blocks = _swig_property(_cv.CvGraph_free_blocks_get, _cv.CvGraph_free_blocks_set)
    __swig_setmethods__["first"] = _cv.CvGraph_first_set
    __swig_getmethods__["first"] = _cv.CvGraph_first_get
    if _newclass:first = _swig_property(_cv.CvGraph_first_get, _cv.CvGraph_first_set)
    __swig_setmethods__["free_elems"] = _cv.CvGraph_free_elems_set
    __swig_getmethods__["free_elems"] = _cv.CvGraph_free_elems_get
    if _newclass:free_elems = _swig_property(_cv.CvGraph_free_elems_get, _cv.CvGraph_free_elems_set)
    __swig_setmethods__["active_count"] = _cv.CvGraph_active_count_set
    __swig_getmethods__["active_count"] = _cv.CvGraph_active_count_get
    if _newclass:active_count = _swig_property(_cv.CvGraph_active_count_get, _cv.CvGraph_active_count_set)
    __swig_setmethods__["edges"] = _cv.CvGraph_edges_set
    __swig_getmethods__["edges"] = _cv.CvGraph_edges_get
    if _newclass:edges = _swig_property(_cv.CvGraph_edges_get, _cv.CvGraph_edges_set)
    def __init__(self, *args): 
        """__init__(self) -> CvGraph"""
        this = _cv.new_CvGraph(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvGraph
    __del__ = lambda self : None;
CvGraph_swigregister = _cv.CvGraph_swigregister
CvGraph_swigregister(CvGraph)

class CvChain(_object):
    """Proxy of C++ CvChain class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvChain, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvChain, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvChain_flags_set
    __swig_getmethods__["flags"] = _cv.CvChain_flags_get
    if _newclass:flags = _swig_property(_cv.CvChain_flags_get, _cv.CvChain_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvChain_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvChain_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvChain_header_size_get, _cv.CvChain_header_size_set)
    __swig_setmethods__["h_prev"] = _cv.CvChain_h_prev_set
    __swig_getmethods__["h_prev"] = _cv.CvChain_h_prev_get
    if _newclass:h_prev = _swig_property(_cv.CvChain_h_prev_get, _cv.CvChain_h_prev_set)
    __swig_setmethods__["h_next"] = _cv.CvChain_h_next_set
    __swig_getmethods__["h_next"] = _cv.CvChain_h_next_get
    if _newclass:h_next = _swig_property(_cv.CvChain_h_next_get, _cv.CvChain_h_next_set)
    __swig_setmethods__["v_prev"] = _cv.CvChain_v_prev_set
    __swig_getmethods__["v_prev"] = _cv.CvChain_v_prev_get
    if _newclass:v_prev = _swig_property(_cv.CvChain_v_prev_get, _cv.CvChain_v_prev_set)
    __swig_setmethods__["v_next"] = _cv.CvChain_v_next_set
    __swig_getmethods__["v_next"] = _cv.CvChain_v_next_get
    if _newclass:v_next = _swig_property(_cv.CvChain_v_next_get, _cv.CvChain_v_next_set)
    __swig_setmethods__["total"] = _cv.CvChain_total_set
    __swig_getmethods__["total"] = _cv.CvChain_total_get
    if _newclass:total = _swig_property(_cv.CvChain_total_get, _cv.CvChain_total_set)
    __swig_setmethods__["elem_size"] = _cv.CvChain_elem_size_set
    __swig_getmethods__["elem_size"] = _cv.CvChain_elem_size_get
    if _newclass:elem_size = _swig_property(_cv.CvChain_elem_size_get, _cv.CvChain_elem_size_set)
    __swig_setmethods__["block_max"] = _cv.CvChain_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvChain_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvChain_block_max_get, _cv.CvChain_block_max_set)
    __swig_setmethods__["ptr"] = _cv.CvChain_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvChain_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvChain_ptr_get, _cv.CvChain_ptr_set)
    __swig_setmethods__["delta_elems"] = _cv.CvChain_delta_elems_set
    __swig_getmethods__["delta_elems"] = _cv.CvChain_delta_elems_get
    if _newclass:delta_elems = _swig_property(_cv.CvChain_delta_elems_get, _cv.CvChain_delta_elems_set)
    __swig_setmethods__["storage"] = _cv.CvChain_storage_set
    __swig_getmethods__["storage"] = _cv.CvChain_storage_get
    if _newclass:storage = _swig_property(_cv.CvChain_storage_get, _cv.CvChain_storage_set)
    __swig_setmethods__["free_blocks"] = _cv.CvChain_free_blocks_set
    __swig_getmethods__["free_blocks"] = _cv.CvChain_free_blocks_get
    if _newclass:free_blocks = _swig_property(_cv.CvChain_free_blocks_get, _cv.CvChain_free_blocks_set)
    __swig_setmethods__["first"] = _cv.CvChain_first_set
    __swig_getmethods__["first"] = _cv.CvChain_first_get
    if _newclass:first = _swig_property(_cv.CvChain_first_get, _cv.CvChain_first_set)
    __swig_setmethods__["origin"] = _cv.CvChain_origin_set
    __swig_getmethods__["origin"] = _cv.CvChain_origin_get
    if _newclass:origin = _swig_property(_cv.CvChain_origin_get, _cv.CvChain_origin_set)
    def __init__(self, *args): 
        """__init__(self) -> CvChain"""
        this = _cv.new_CvChain(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvChain
    __del__ = lambda self : None;
CvChain_swigregister = _cv.CvChain_swigregister
CvChain_swigregister(CvChain)

class CvContour(_object):
    """Proxy of C++ CvContour class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvContour, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvContour, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvContour_flags_set
    __swig_getmethods__["flags"] = _cv.CvContour_flags_get
    if _newclass:flags = _swig_property(_cv.CvContour_flags_get, _cv.CvContour_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvContour_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvContour_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvContour_header_size_get, _cv.CvContour_header_size_set)
    __swig_setmethods__["h_prev"] = _cv.CvContour_h_prev_set
    __swig_getmethods__["h_prev"] = _cv.CvContour_h_prev_get
    if _newclass:h_prev = _swig_property(_cv.CvContour_h_prev_get, _cv.CvContour_h_prev_set)
    __swig_setmethods__["h_next"] = _cv.CvContour_h_next_set
    __swig_getmethods__["h_next"] = _cv.CvContour_h_next_get
    if _newclass:h_next = _swig_property(_cv.CvContour_h_next_get, _cv.CvContour_h_next_set)
    __swig_setmethods__["v_prev"] = _cv.CvContour_v_prev_set
    __swig_getmethods__["v_prev"] = _cv.CvContour_v_prev_get
    if _newclass:v_prev = _swig_property(_cv.CvContour_v_prev_get, _cv.CvContour_v_prev_set)
    __swig_setmethods__["v_next"] = _cv.CvContour_v_next_set
    __swig_getmethods__["v_next"] = _cv.CvContour_v_next_get
    if _newclass:v_next = _swig_property(_cv.CvContour_v_next_get, _cv.CvContour_v_next_set)
    __swig_setmethods__["total"] = _cv.CvContour_total_set
    __swig_getmethods__["total"] = _cv.CvContour_total_get
    if _newclass:total = _swig_property(_cv.CvContour_total_get, _cv.CvContour_total_set)
    __swig_setmethods__["elem_size"] = _cv.CvContour_elem_size_set
    __swig_getmethods__["elem_size"] = _cv.CvContour_elem_size_get
    if _newclass:elem_size = _swig_property(_cv.CvContour_elem_size_get, _cv.CvContour_elem_size_set)
    __swig_setmethods__["block_max"] = _cv.CvContour_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvContour_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvContour_block_max_get, _cv.CvContour_block_max_set)
    __swig_setmethods__["ptr"] = _cv.CvContour_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvContour_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvContour_ptr_get, _cv.CvContour_ptr_set)
    __swig_setmethods__["delta_elems"] = _cv.CvContour_delta_elems_set
    __swig_getmethods__["delta_elems"] = _cv.CvContour_delta_elems_get
    if _newclass:delta_elems = _swig_property(_cv.CvContour_delta_elems_get, _cv.CvContour_delta_elems_set)
    __swig_setmethods__["storage"] = _cv.CvContour_storage_set
    __swig_getmethods__["storage"] = _cv.CvContour_storage_get
    if _newclass:storage = _swig_property(_cv.CvContour_storage_get, _cv.CvContour_storage_set)
    __swig_setmethods__["free_blocks"] = _cv.CvContour_free_blocks_set
    __swig_getmethods__["free_blocks"] = _cv.CvContour_free_blocks_get
    if _newclass:free_blocks = _swig_property(_cv.CvContour_free_blocks_get, _cv.CvContour_free_blocks_set)
    __swig_setmethods__["first"] = _cv.CvContour_first_set
    __swig_getmethods__["first"] = _cv.CvContour_first_get
    if _newclass:first = _swig_property(_cv.CvContour_first_get, _cv.CvContour_first_set)
    __swig_setmethods__["rect"] = _cv.CvContour_rect_set
    __swig_getmethods__["rect"] = _cv.CvContour_rect_get
    if _newclass:rect = _swig_property(_cv.CvContour_rect_get, _cv.CvContour_rect_set)
    __swig_setmethods__["color"] = _cv.CvContour_color_set
    __swig_getmethods__["color"] = _cv.CvContour_color_get
    if _newclass:color = _swig_property(_cv.CvContour_color_get, _cv.CvContour_color_set)
    __swig_setmethods__["reserved"] = _cv.CvContour_reserved_set
    __swig_getmethods__["reserved"] = _cv.CvContour_reserved_get
    if _newclass:reserved = _swig_property(_cv.CvContour_reserved_get, _cv.CvContour_reserved_set)
    def __init__(self, *args): 
        """__init__(self) -> CvContour"""
        this = _cv.new_CvContour(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvContour
    __del__ = lambda self : None;
CvContour_swigregister = _cv.CvContour_swigregister
CvContour_swigregister(CvContour)

class CvSeqWriter(_object):
    """Proxy of C++ CvSeqWriter class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeqWriter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeqWriter, name)
    __repr__ = _swig_repr
    __swig_setmethods__["header_size"] = _cv.CvSeqWriter_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvSeqWriter_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvSeqWriter_header_size_get, _cv.CvSeqWriter_header_size_set)
    __swig_setmethods__["seq"] = _cv.CvSeqWriter_seq_set
    __swig_getmethods__["seq"] = _cv.CvSeqWriter_seq_get
    if _newclass:seq = _swig_property(_cv.CvSeqWriter_seq_get, _cv.CvSeqWriter_seq_set)
    __swig_setmethods__["block"] = _cv.CvSeqWriter_block_set
    __swig_getmethods__["block"] = _cv.CvSeqWriter_block_get
    if _newclass:block = _swig_property(_cv.CvSeqWriter_block_get, _cv.CvSeqWriter_block_set)
    __swig_setmethods__["ptr"] = _cv.CvSeqWriter_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvSeqWriter_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvSeqWriter_ptr_get, _cv.CvSeqWriter_ptr_set)
    __swig_setmethods__["block_min"] = _cv.CvSeqWriter_block_min_set
    __swig_getmethods__["block_min"] = _cv.CvSeqWriter_block_min_get
    if _newclass:block_min = _swig_property(_cv.CvSeqWriter_block_min_get, _cv.CvSeqWriter_block_min_set)
    __swig_setmethods__["block_max"] = _cv.CvSeqWriter_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvSeqWriter_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvSeqWriter_block_max_get, _cv.CvSeqWriter_block_max_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSeqWriter"""
        this = _cv.new_CvSeqWriter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeqWriter
    __del__ = lambda self : None;
CvSeqWriter_swigregister = _cv.CvSeqWriter_swigregister
CvSeqWriter_swigregister(CvSeqWriter)

class CvSeqReader(_object):
    """Proxy of C++ CvSeqReader class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeqReader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeqReader, name)
    __repr__ = _swig_repr
    __swig_setmethods__["header_size"] = _cv.CvSeqReader_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvSeqReader_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvSeqReader_header_size_get, _cv.CvSeqReader_header_size_set)
    __swig_setmethods__["seq"] = _cv.CvSeqReader_seq_set
    __swig_getmethods__["seq"] = _cv.CvSeqReader_seq_get
    if _newclass:seq = _swig_property(_cv.CvSeqReader_seq_get, _cv.CvSeqReader_seq_set)
    __swig_setmethods__["block"] = _cv.CvSeqReader_block_set
    __swig_getmethods__["block"] = _cv.CvSeqReader_block_get
    if _newclass:block = _swig_property(_cv.CvSeqReader_block_get, _cv.CvSeqReader_block_set)
    __swig_setmethods__["ptr"] = _cv.CvSeqReader_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvSeqReader_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvSeqReader_ptr_get, _cv.CvSeqReader_ptr_set)
    __swig_setmethods__["block_min"] = _cv.CvSeqReader_block_min_set
    __swig_getmethods__["block_min"] = _cv.CvSeqReader_block_min_get
    if _newclass:block_min = _swig_property(_cv.CvSeqReader_block_min_get, _cv.CvSeqReader_block_min_set)
    __swig_setmethods__["block_max"] = _cv.CvSeqReader_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvSeqReader_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvSeqReader_block_max_get, _cv.CvSeqReader_block_max_set)
    __swig_setmethods__["delta_index"] = _cv.CvSeqReader_delta_index_set
    __swig_getmethods__["delta_index"] = _cv.CvSeqReader_delta_index_get
    if _newclass:delta_index = _swig_property(_cv.CvSeqReader_delta_index_get, _cv.CvSeqReader_delta_index_set)
    __swig_setmethods__["prev_elem"] = _cv.CvSeqReader_prev_elem_set
    __swig_getmethods__["prev_elem"] = _cv.CvSeqReader_prev_elem_get
    if _newclass:prev_elem = _swig_property(_cv.CvSeqReader_prev_elem_get, _cv.CvSeqReader_prev_elem_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSeqReader"""
        this = _cv.new_CvSeqReader(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeqReader
    __del__ = lambda self : None;
CvSeqReader_swigregister = _cv.CvSeqReader_swigregister
CvSeqReader_swigregister(CvSeqReader)

class CvAttrList(_object):
    """Proxy of C++ CvAttrList class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvAttrList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvAttrList, name)
    __repr__ = _swig_repr
    __swig_setmethods__["attr"] = _cv.CvAttrList_attr_set
    __swig_getmethods__["attr"] = _cv.CvAttrList_attr_get
    if _newclass:attr = _swig_property(_cv.CvAttrList_attr_get, _cv.CvAttrList_attr_set)
    __swig_setmethods__["next"] = _cv.CvAttrList_next_set
    __swig_getmethods__["next"] = _cv.CvAttrList_next_get
    if _newclass:next = _swig_property(_cv.CvAttrList_next_get, _cv.CvAttrList_next_set)
    def __init__(self, *args): 
        """__init__(self) -> CvAttrList"""
        this = _cv.new_CvAttrList(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvAttrList
    __del__ = lambda self : None;
CvAttrList_swigregister = _cv.CvAttrList_swigregister
CvAttrList_swigregister(CvAttrList)

class CvString(_object):
    """Proxy of C++ CvString class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvString, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvString, name)
    __repr__ = _swig_repr
    __swig_setmethods__["len"] = _cv.CvString_len_set
    __swig_getmethods__["len"] = _cv.CvString_len_get
    if _newclass:len = _swig_property(_cv.CvString_len_get, _cv.CvString_len_set)
    __swig_setmethods__["ptr"] = _cv.CvString_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvString_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvString_ptr_get, _cv.CvString_ptr_set)
    def __init__(self, *args): 
        """__init__(self) -> CvString"""
        this = _cv.new_CvString(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvString
    __del__ = lambda self : None;
CvString_swigregister = _cv.CvString_swigregister
CvString_swigregister(CvString)

def cvAttrList(*args):
  """
    cvAttrList(char attr=None, CvAttrList next=None) -> CvAttrList
    cvAttrList(char attr=None) -> CvAttrList
    cvAttrList() -> CvAttrList
    """
  return _cv.cvAttrList(*args)

class CvStringHashNode(_object):
    """Proxy of C++ CvStringHashNode class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvStringHashNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvStringHashNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hashval"] = _cv.CvStringHashNode_hashval_set
    __swig_getmethods__["hashval"] = _cv.CvStringHashNode_hashval_get
    if _newclass:hashval = _swig_property(_cv.CvStringHashNode_hashval_get, _cv.CvStringHashNode_hashval_set)
    __swig_setmethods__["str"] = _cv.CvStringHashNode_str_set
    __swig_getmethods__["str"] = _cv.CvStringHashNode_str_get
    if _newclass:str = _swig_property(_cv.CvStringHashNode_str_get, _cv.CvStringHashNode_str_set)
    __swig_setmethods__["next"] = _cv.CvStringHashNode_next_set
    __swig_getmethods__["next"] = _cv.CvStringHashNode_next_get
    if _newclass:next = _swig_property(_cv.CvStringHashNode_next_get, _cv.CvStringHashNode_next_set)
    def __init__(self, *args): 
        """__init__(self) -> CvStringHashNode"""
        this = _cv.new_CvStringHashNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvStringHashNode
    __del__ = lambda self : None;
CvStringHashNode_swigregister = _cv.CvStringHashNode_swigregister
CvStringHashNode_swigregister(CvStringHashNode)

class CvFileNode(_object):
    """Proxy of C++ CvFileNode class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvFileNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvFileNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tag"] = _cv.CvFileNode_tag_set
    __swig_getmethods__["tag"] = _cv.CvFileNode_tag_get
    if _newclass:tag = _swig_property(_cv.CvFileNode_tag_get, _cv.CvFileNode_tag_set)
    __swig_setmethods__["info"] = _cv.CvFileNode_info_set
    __swig_getmethods__["info"] = _cv.CvFileNode_info_get
    if _newclass:info = _swig_property(_cv.CvFileNode_info_get, _cv.CvFileNode_info_set)
    __swig_getmethods__["data"] = _cv.CvFileNode_data_get
    if _newclass:data = _swig_property(_cv.CvFileNode_data_get)
    def __init__(self, *args): 
        """__init__(self) -> CvFileNode"""
        this = _cv.new_CvFileNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvFileNode
    __del__ = lambda self : None;
CvFileNode_swigregister = _cv.CvFileNode_swigregister
CvFileNode_swigregister(CvFileNode)

class CvFileNode_data(_object):
    """Proxy of C++ CvFileNode_data class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvFileNode_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvFileNode_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["f"] = _cv.CvFileNode_data_f_set
    __swig_getmethods__["f"] = _cv.CvFileNode_data_f_get
    if _newclass:f = _swig_property(_cv.CvFileNode_data_f_get, _cv.CvFileNode_data_f_set)
    __swig_setmethods__["i"] = _cv.CvFileNode_data_i_set
    __swig_getmethods__["i"] = _cv.CvFileNode_data_i_get
    if _newclass:i = _swig_property(_cv.CvFileNode_data_i_get, _cv.CvFileNode_data_i_set)
    __swig_setmethods__["str"] = _cv.CvFileNode_data_str_set
    __swig_getmethods__["str"] = _cv.CvFileNode_data_str_get
    if _newclass:str = _swig_property(_cv.CvFileNode_data_str_get, _cv.CvFileNode_data_str_set)
    __swig_setmethods__["seq"] = _cv.CvFileNode_data_seq_set
    __swig_getmethods__["seq"] = _cv.CvFileNode_data_seq_get
    if _newclass:seq = _swig_property(_cv.CvFileNode_data_seq_get, _cv.CvFileNode_data_seq_set)
    __swig_setmethods__["map"] = _cv.CvFileNode_data_map_set
    __swig_getmethods__["map"] = _cv.CvFileNode_data_map_get
    if _newclass:map = _swig_property(_cv.CvFileNode_data_map_get, _cv.CvFileNode_data_map_set)
    def __init__(self, *args): 
        """__init__(self) -> CvFileNode_data"""
        this = _cv.new_CvFileNode_data(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvFileNode_data
    __del__ = lambda self : None;
CvFileNode_data_swigregister = _cv.CvFileNode_data_swigregister
CvFileNode_data_swigregister(CvFileNode_data)

class CvTypeInfo(_object):
    """Proxy of C++ CvTypeInfo class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvTypeInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvTypeInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvTypeInfo_flags_set
    __swig_getmethods__["flags"] = _cv.CvTypeInfo_flags_get
    if _newclass:flags = _swig_property(_cv.CvTypeInfo_flags_get, _cv.CvTypeInfo_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvTypeInfo_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvTypeInfo_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvTypeInfo_header_size_get, _cv.CvTypeInfo_header_size_set)
    __swig_setmethods__["prev"] = _cv.CvTypeInfo_prev_set
    __swig_getmethods__["prev"] = _cv.CvTypeInfo_prev_get
    if _newclass:prev = _swig_property(_cv.CvTypeInfo_prev_get, _cv.CvTypeInfo_prev_set)
    __swig_setmethods__["next"] = _cv.CvTypeInfo_next_set
    __swig_getmethods__["next"] = _cv.CvTypeInfo_next_get
    if _newclass:next = _swig_property(_cv.CvTypeInfo_next_get, _cv.CvTypeInfo_next_set)
    __swig_setmethods__["type_name"] = _cv.CvTypeInfo_type_name_set
    __swig_getmethods__["type_name"] = _cv.CvTypeInfo_type_name_get
    if _newclass:type_name = _swig_property(_cv.CvTypeInfo_type_name_get, _cv.CvTypeInfo_type_name_set)
    __swig_setmethods__["is_instance"] = _cv.CvTypeInfo_is_instance_set
    __swig_getmethods__["is_instance"] = _cv.CvTypeInfo_is_instance_get
    if _newclass:is_instance = _swig_property(_cv.CvTypeInfo_is_instance_get, _cv.CvTypeInfo_is_instance_set)
    __swig_setmethods__["release"] = _cv.CvTypeInfo_release_set
    __swig_getmethods__["release"] = _cv.CvTypeInfo_release_get
    if _newclass:release = _swig_property(_cv.CvTypeInfo_release_get, _cv.CvTypeInfo_release_set)
    __swig_setmethods__["read"] = _cv.CvTypeInfo_read_set
    __swig_getmethods__["read"] = _cv.CvTypeInfo_read_get
    if _newclass:read = _swig_property(_cv.CvTypeInfo_read_get, _cv.CvTypeInfo_read_set)
    __swig_setmethods__["write"] = _cv.CvTypeInfo_write_set
    __swig_getmethods__["write"] = _cv.CvTypeInfo_write_get
    if _newclass:write = _swig_property(_cv.CvTypeInfo_write_get, _cv.CvTypeInfo_write_set)
    __swig_setmethods__["clone"] = _cv.CvTypeInfo_clone_set
    __swig_getmethods__["clone"] = _cv.CvTypeInfo_clone_get
    if _newclass:clone = _swig_property(_cv.CvTypeInfo_clone_get, _cv.CvTypeInfo_clone_set)
    def __init__(self, *args): 
        """__init__(self) -> CvTypeInfo"""
        this = _cv.new_CvTypeInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvTypeInfo
    __del__ = lambda self : None;
CvTypeInfo_swigregister = _cv.CvTypeInfo_swigregister
CvTypeInfo_swigregister(CvTypeInfo)

class CvPluginFuncInfo(_object):
    """Proxy of C++ CvPluginFuncInfo class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvPluginFuncInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvPluginFuncInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["func_addr"] = _cv.CvPluginFuncInfo_func_addr_set
    __swig_getmethods__["func_addr"] = _cv.CvPluginFuncInfo_func_addr_get
    if _newclass:func_addr = _swig_property(_cv.CvPluginFuncInfo_func_addr_get, _cv.CvPluginFuncInfo_func_addr_set)
    __swig_setmethods__["default_func_addr"] = _cv.CvPluginFuncInfo_default_func_addr_set
    __swig_getmethods__["default_func_addr"] = _cv.CvPluginFuncInfo_default_func_addr_get
    if _newclass:default_func_addr = _swig_property(_cv.CvPluginFuncInfo_default_func_addr_get, _cv.CvPluginFuncInfo_default_func_addr_set)
    __swig_setmethods__["func_names"] = _cv.CvPluginFuncInfo_func_names_set
    __swig_getmethods__["func_names"] = _cv.CvPluginFuncInfo_func_names_get
    if _newclass:func_names = _swig_property(_cv.CvPluginFuncInfo_func_names_get, _cv.CvPluginFuncInfo_func_names_set)
    __swig_setmethods__["search_modules"] = _cv.CvPluginFuncInfo_search_modules_set
    __swig_getmethods__["search_modules"] = _cv.CvPluginFuncInfo_search_modules_get
    if _newclass:search_modules = _swig_property(_cv.CvPluginFuncInfo_search_modules_get, _cv.CvPluginFuncInfo_search_modules_set)
    __swig_setmethods__["loaded_from"] = _cv.CvPluginFuncInfo_loaded_from_set
    __swig_getmethods__["loaded_from"] = _cv.CvPluginFuncInfo_loaded_from_get
    if _newclass:loaded_from = _swig_property(_cv.CvPluginFuncInfo_loaded_from_get, _cv.CvPluginFuncInfo_loaded_from_set)
    def __init__(self, *args): 
        """__init__(self) -> CvPluginFuncInfo"""
        this = _cv.new_CvPluginFuncInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvPluginFuncInfo
    __del__ = lambda self : None;
CvPluginFuncInfo_swigregister = _cv.CvPluginFuncInfo_swigregister
CvPluginFuncInfo_swigregister(CvPluginFuncInfo)

class CvModuleInfo(_object):
    """Proxy of C++ CvModuleInfo class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvModuleInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvModuleInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["next"] = _cv.CvModuleInfo_next_set
    __swig_getmethods__["next"] = _cv.CvModuleInfo_next_get
    if _newclass:next = _swig_property(_cv.CvModuleInfo_next_get, _cv.CvModuleInfo_next_set)
    __swig_setmethods__["name"] = _cv.CvModuleInfo_name_set
    __swig_getmethods__["name"] = _cv.CvModuleInfo_name_get
    if _newclass:name = _swig_property(_cv.CvModuleInfo_name_get, _cv.CvModuleInfo_name_set)
    __swig_setmethods__["version"] = _cv.CvModuleInfo_version_set
    __swig_getmethods__["version"] = _cv.CvModuleInfo_version_get
    if _newclass:version = _swig_property(_cv.CvModuleInfo_version_get, _cv.CvModuleInfo_version_set)
    __swig_setmethods__["func_tab"] = _cv.CvModuleInfo_func_tab_set
    __swig_getmethods__["func_tab"] = _cv.CvModuleInfo_func_tab_get
    if _newclass:func_tab = _swig_property(_cv.CvModuleInfo_func_tab_get, _cv.CvModuleInfo_func_tab_set)
    def __init__(self, *args): 
        """__init__(self) -> CvModuleInfo"""
        this = _cv.new_CvModuleInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvModuleInfo
    __del__ = lambda self : None;
CvModuleInfo_swigregister = _cv.CvModuleInfo_swigregister
CvModuleInfo_swigregister(CvModuleInfo)


def cvAlloc(*args):
  """cvAlloc(size_t size) -> void"""
  return _cv.cvAlloc(*args)

def cvFree_(*args):
  """cvFree_(void ptr)"""
  return _cv.cvFree_(*args)

def cvResetImageROI(*args):
  """cvResetImageROI( image)"""
  return _cv.cvResetImageROI(*args)

def cvCreateMatHeader(*args):
  """cvCreateMatHeader(int rows, int cols, int type) -> CvMat"""
  return _cv.cvCreateMatHeader(*args)

def cvInitMatHeader(*args):
  """
    cvInitMatHeader(CvMat mat, int rows, int cols, int type, void data=None, 
        int step=0x7fffffff) -> CvMat
    """
  return _cv.cvInitMatHeader(*args)

def cvCreateMat(*args):
  """cvCreateMat(int rows, int cols, int type) -> CvMat"""
  return _cv.cvCreateMat(*args)

def cvDecRefData(*args):
  """cvDecRefData(CvArr arr)"""
  return _cv.cvDecRefData(*args)

def cvIncRefData(*args):
  """cvIncRefData(CvArr arr) -> int"""
  return _cv.cvIncRefData(*args)

def cvCloneMat(*args):
  """cvCloneMat(CvMat mat) -> CvMat"""
  return _cv.cvCloneMat(*args)

def cvGetSubRect(*args):
  """cvGetSubRect(CvArr arr, CvMat submat, CvRect rect) -> CvMat"""
  return _cv.cvGetSubRect(*args)

def cvGetRows(*args):
  """
    cvGetRows(CvArr arr, CvMat submat, int start_row, int end_row, 
        int delta_row=1) -> CvMat
    """
  return _cv.cvGetRows(*args)

def cvGetRow(*args):
  """cvGetRow(CvArr arr, CvMat submat, int row) -> CvMat"""
  return _cv.cvGetRow(*args)

def cvGetCols(*args):
  """cvGetCols(CvArr arr, CvMat submat, int start_col, int end_col) -> CvMat"""
  return _cv.cvGetCols(*args)

def cvGetCol(*args):
  """cvGetCol(CvArr arr, CvMat submat, int col) -> CvMat"""
  return _cv.cvGetCol(*args)

def cvGetDiag(*args):
  """cvGetDiag(CvArr arr, CvMat submat, int diag=0) -> CvMat"""
  return _cv.cvGetDiag(*args)

def cvScalarToRawData(*args):
  """cvScalarToRawData(CvScalar scalar, void data, int type, int extend_to_12=0)"""
  return _cv.cvScalarToRawData(*args)

def cvRawDataToScalar(*args):
  """cvRawDataToScalar(void data, int type, CvScalar scalar)"""
  return _cv.cvRawDataToScalar(*args)

def cvCreateMatNDHeader(*args):
  """cvCreateMatNDHeader(int dims, int type) -> CvMatND"""
  return _cv.cvCreateMatNDHeader(*args)

def cvCreateMatND(*args):
  """cvCreateMatND(int dims, int type) -> CvMatND"""
  return _cv.cvCreateMatND(*args)

def cvInitMatNDHeader(*args):
  """cvInitMatNDHeader(CvMatND mat, int dims, int type, void data=None) -> CvMatND"""
  return _cv.cvInitMatNDHeader(*args)

def cvCloneMatND(*args):
  """cvCloneMatND(CvMatND mat) -> CvMatND"""
  return _cv.cvCloneMatND(*args)

def cvCreateSparseMat(*args):
  """cvCreateSparseMat(int dims, int type) -> CvSparseMat"""
  return _cv.cvCreateSparseMat(*args)

def cvCloneSparseMat(*args):
  """cvCloneSparseMat(CvSparseMat mat) -> CvSparseMat"""
  return _cv.cvCloneSparseMat(*args)

def cvInitSparseMatIterator(*args):
  """cvInitSparseMatIterator(CvSparseMat mat, CvSparseMatIterator mat_iterator) -> CvSparseNode"""
  return _cv.cvInitSparseMatIterator(*args)

def cvGetNextSparseNode(*args):
  """cvGetNextSparseNode(CvSparseMatIterator mat_iterator) -> CvSparseNode"""
  return _cv.cvGetNextSparseNode(*args)
class CvNArrayIterator(_object):
    """Proxy of C++ CvNArrayIterator class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvNArrayIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvNArrayIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["count"] = _cv.CvNArrayIterator_count_set
    __swig_getmethods__["count"] = _cv.CvNArrayIterator_count_get
    if _newclass:count = _swig_property(_cv.CvNArrayIterator_count_get, _cv.CvNArrayIterator_count_set)
    __swig_setmethods__["dims"] = _cv.CvNArrayIterator_dims_set
    __swig_getmethods__["dims"] = _cv.CvNArrayIterator_dims_get
    if _newclass:dims = _swig_property(_cv.CvNArrayIterator_dims_get, _cv.CvNArrayIterator_dims_set)
    __swig_setmethods__["size"] = _cv.CvNArrayIterator_size_set
    __swig_getmethods__["size"] = _cv.CvNArrayIterator_size_get
    if _newclass:size = _swig_property(_cv.CvNArrayIterator_size_get, _cv.CvNArrayIterator_size_set)
    __swig_setmethods__["ptr"] = _cv.CvNArrayIterator_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvNArrayIterator_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvNArrayIterator_ptr_get, _cv.CvNArrayIterator_ptr_set)
    __swig_setmethods__["stack"] = _cv.CvNArrayIterator_stack_set
    __swig_getmethods__["stack"] = _cv.CvNArrayIterator_stack_get
    if _newclass:stack = _swig_property(_cv.CvNArrayIterator_stack_get, _cv.CvNArrayIterator_stack_set)
    __swig_setmethods__["hdr"] = _cv.CvNArrayIterator_hdr_set
    __swig_getmethods__["hdr"] = _cv.CvNArrayIterator_hdr_get
    if _newclass:hdr = _swig_property(_cv.CvNArrayIterator_hdr_get, _cv.CvNArrayIterator_hdr_set)
    def __init__(self, *args): 
        """__init__(self) -> CvNArrayIterator"""
        this = _cv.new_CvNArrayIterator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvNArrayIterator
    __del__ = lambda self : None;
CvNArrayIterator_swigregister = _cv.CvNArrayIterator_swigregister
CvNArrayIterator_swigregister(CvNArrayIterator)


def cvInitNArrayIterator(*args):
  """
    cvInitNArrayIterator(int count, CvArr arrs, CvArr mask, CvMatND stubs, CvNArrayIterator array_iterator, 
        int flags=0) -> int
    """
  return _cv.cvInitNArrayIterator(*args)

def cvNextNArraySlice(*args):
  """cvNextNArraySlice(CvNArrayIterator array_iterator) -> int"""
  return _cv.cvNextNArraySlice(*args)

def cvGetElemType(*args):
  """cvGetElemType(CvArr arr) -> int"""
  return _cv.cvGetElemType(*args)

def cvGetDims(*args):
  """cvGetDims(CvArr arr) -> int"""
  return _cv.cvGetDims(*args)

def cvGetDimSize(*args):
  """cvGetDimSize(CvArr arr, int index) -> int"""
  return _cv.cvGetDimSize(*args)

def cvPtr1D(*args):
  """cvPtr1D(CvArr arr, int idx0, int type=None) -> uchar"""
  return _cv.cvPtr1D(*args)

def cvPtr2D(*args):
  """cvPtr2D(CvArr arr, int idx0, int idx1, int type=None) -> uchar"""
  return _cv.cvPtr2D(*args)

def cvPtr3D(*args):
  """cvPtr3D(CvArr arr, int idx0, int idx1, int idx2, int type=None) -> uchar"""
  return _cv.cvPtr3D(*args)

def cvPtrND(*args):
  """
    cvPtrND(CvArr arr, int idx, int type=None, int create_node=1, 
        unsigned int precalc_hashval=None) -> uchar
    """
  return _cv.cvPtrND(*args)

def cvGet1D(*args):
  """cvGet1D(CvArr arr, int idx0) -> CvScalar"""
  return _cv.cvGet1D(*args)

def cvGet2D(*args):
  """cvGet2D(CvArr arr, int idx0, int idx1) -> CvScalar"""
  return _cv.cvGet2D(*args)

def cvGet3D(*args):
  """cvGet3D(CvArr arr, int idx0, int idx1, int idx2) -> CvScalar"""
  return _cv.cvGet3D(*args)

def cvGetND(*args):
  """cvGetND(CvArr arr, int idx) -> CvScalar"""
  return _cv.cvGetND(*args)

def cvGetReal1D(*args):
  """cvGetReal1D(CvArr arr, int idx0) -> double"""
  return _cv.cvGetReal1D(*args)

def cvGetReal2D(*args):
  """cvGetReal2D(CvArr arr, int idx0, int idx1) -> double"""
  return _cv.cvGetReal2D(*args)

def cvGetReal3D(*args):
  """cvGetReal3D(CvArr arr, int idx0, int idx1, int idx2) -> double"""
  return _cv.cvGetReal3D(*args)

def cvGetRealND(*args):
  """cvGetRealND(CvArr arr, int idx) -> double"""
  return _cv.cvGetRealND(*args)

def cvSet1D(*args):
  """cvSet1D(CvArr arr, int idx0, CvScalar value)"""
  return _cv.cvSet1D(*args)

def cvSet2D(*args):
  """cvSet2D(CvArr arr, int idx0, int idx1, CvScalar value)"""
  return _cv.cvSet2D(*args)

def cvSet3D(*args):
  """cvSet3D(CvArr arr, int idx0, int idx1, int idx2, CvScalar value)"""
  return _cv.cvSet3D(*args)

def cvSetND(*args):
  """cvSetND(CvArr arr, int idx, CvScalar value)"""
  return _cv.cvSetND(*args)

def cvSetReal1D(*args):
  """cvSetReal1D(CvArr arr, int idx0, double value)"""
  return _cv.cvSetReal1D(*args)

def cvSetReal2D(*args):
  """cvSetReal2D(CvArr arr, int idx0, int idx1, double value)"""
  return _cv.cvSetReal2D(*args)

def cvSetReal3D(*args):
  """cvSetReal3D(CvArr arr, int idx0, int idx1, int idx2, double value)"""
  return _cv.cvSetReal3D(*args)

def cvSetRealND(*args):
  """cvSetRealND(CvArr arr, int idx, double value)"""
  return _cv.cvSetRealND(*args)

def cvClearND(*args):
  """cvClearND(CvArr arr, int idx)"""
  return _cv.cvClearND(*args)

def cvGetMat(*args):
  """cvGetMat(CvArr arr, CvMat header, int coi=None, int allowND=0) -> CvMat"""
  return _cv.cvGetMat(*args)

def cvReshapeMatND(*args):
  """
    cvReshapeMatND(CvArr arr, int sizeof_header, CvArr header, int new_cn, 
        int new_dims, int new_sizes) -> CvArr
    """
  return _cv.cvReshapeMatND(*args)

def cvReshape(*args):
  """cvReshape(CvArr arr, CvMat header, int new_cn, int new_rows=0) -> CvMat"""
  return _cv.cvReshape(*args)

def cvRepeat(*args):
  """cvRepeat(CvArr src, CvArr dst)"""
  return _cv.cvRepeat(*args)

def cvCreateData(*args):
  """cvCreateData(CvArr arr)"""
  return _cv.cvCreateData(*args)

def cvReleaseData(*args):
  """cvReleaseData(CvArr arr)"""
  return _cv.cvReleaseData(*args)

def cvSetData(*args):
  """cvSetData(CvArr arr, void data, int step)"""
  return _cv.cvSetData(*args)

def cvGetRawData(*args):
  """cvGetRawData(CvArr arr, uchar data, int step=None, CvSize roi_size=None)"""
  return _cv.cvGetRawData(*args)

def cvGetSize(*args):
  """cvGetSize(CvArr arr) -> CvSize"""
  return _cv.cvGetSize(*args)

def cvCopy(*args):
  """cvCopy(CvArr src, CvArr dst, CvArr mask=None)"""
  return _cv.cvCopy(*args)

def cvSet(*args):
  """cvSet(CvArr arr, CvScalar value, CvArr mask=None)"""
  return _cv.cvSet(*args)

def cvSetZero(*args):
  """cvSetZero(CvArr arr)"""
  return _cv.cvSetZero(*args)

def cvSplit(*args):
  """cvSplit(CvArr src, CvArr dst0, CvArr dst1, CvArr dst2, CvArr dst3)"""
  return _cv.cvSplit(*args)

def cvMerge(*args):
  """cvMerge(CvArr src0, CvArr src1, CvArr src2, CvArr src3, CvArr dst)"""
  return _cv.cvMerge(*args)

def cvMixChannels(*args):
  """
    cvMixChannels(CvArr src, int src_count, CvArr dst, int dst_count, 
        int from_to, int pair_count)
    """
  return _cv.cvMixChannels(*args)

def cvConvertScale(*args):
  """cvConvertScale(CvArr src, CvArr dst, double scale=1, double shift=0)"""
  return _cv.cvConvertScale(*args)

def cvConvertScaleAbs(*args):
  """cvConvertScaleAbs(CvArr src, CvArr dst, double scale=1, double shift=0)"""
  return _cv.cvConvertScaleAbs(*args)

def cvCheckTermCriteria(*args):
  """cvCheckTermCriteria(CvTermCriteria criteria, double default_eps, int default_max_iters) -> CvTermCriteria"""
  return _cv.cvCheckTermCriteria(*args)

def cvAdd(*args):
  """cvAdd(CvArr src1, CvArr src2, CvArr dst, CvArr mask=None)"""
  return _cv.cvAdd(*args)

def cvAddS(*args):
  """cvAddS(CvArr src, CvScalar value, CvArr dst, CvArr mask=None)"""
  return _cv.cvAddS(*args)

def cvSub(*args):
  """cvSub(CvArr src1, CvArr src2, CvArr dst, CvArr mask=None)"""
  return _cv.cvSub(*args)

def cvSubS(*args):
  """cvSubS(CvArr src, CvScalar value, CvArr dst, CvArr mask=None)"""
  return _cv.cvSubS(*args)

def cvSubRS(*args):
  """cvSubRS(CvArr src, CvScalar value, CvArr dst, CvArr mask=None)"""
  return _cv.cvSubRS(*args)

def cvMul(*args):
  """cvMul(CvArr src1, CvArr src2, CvArr dst, double scale=1)"""
  return _cv.cvMul(*args)

def cvDiv(*args):
  """cvDiv(CvArr src1, CvArr src2, CvArr dst, double scale=1)"""
  return _cv.cvDiv(*args)

def cvScaleAdd(*args):
  """cvScaleAdd(CvArr src1, CvScalar scale, CvArr src2, CvArr dst)"""
  return _cv.cvScaleAdd(*args)

def cvAddWeighted(*args):
  """
    cvAddWeighted(CvArr src1, double alpha, CvArr src2, double beta, 
        double gamma, CvArr dst)
    """
  return _cv.cvAddWeighted(*args)

def cvDotProduct(*args):
  """cvDotProduct(CvArr src1, CvArr src2) -> double"""
  return _cv.cvDotProduct(*args)

def cvAnd(*args):
  """cvAnd(CvArr src1, CvArr src2, CvArr dst, CvArr mask=None)"""
  return _cv.cvAnd(*args)

def cvAndS(*args):
  """cvAndS(CvArr src, CvScalar value, CvArr dst, CvArr mask=None)"""
  return _cv.cvAndS(*args)

def cvOr(*args):
  """cvOr(CvArr src1, CvArr src2, CvArr dst, CvArr mask=None)"""
  return _cv.cvOr(*args)

def cvOrS(*args):
  """cvOrS(CvArr src, CvScalar value, CvArr dst, CvArr mask=None)"""
  return _cv.cvOrS(*args)

def cvXor(*args):
  """cvXor(CvArr src1, CvArr src2, CvArr dst, CvArr mask=None)"""
  return _cv.cvXor(*args)

def cvXorS(*args):
  """cvXorS(CvArr src, CvScalar value, CvArr dst, CvArr mask=None)"""
  return _cv.cvXorS(*args)

def cvNot(*args):
  """cvNot(CvArr src, CvArr dst)"""
  return _cv.cvNot(*args)

def cvInRange(*args):
  """cvInRange(CvArr src, CvArr lower, CvArr upper, CvArr dst)"""
  return _cv.cvInRange(*args)

def cvInRangeS(*args):
  """cvInRangeS(CvArr src, CvScalar lower, CvScalar upper, CvArr dst)"""
  return _cv.cvInRangeS(*args)

def cvCmp(*args):
  """cvCmp(CvArr src1, CvArr src2, CvArr dst, int cmp_op)"""
  return _cv.cvCmp(*args)

def cvCmpS(*args):
  """cvCmpS(CvArr src, double value, CvArr dst, int cmp_op)"""
  return _cv.cvCmpS(*args)

def cvMin(*args):
  """cvMin(CvArr src1, CvArr src2, CvArr dst)"""
  return _cv.cvMin(*args)

def cvMax(*args):
  """cvMax(CvArr src1, CvArr src2, CvArr dst)"""
  return _cv.cvMax(*args)

def cvMinS(*args):
  """cvMinS(CvArr src, double value, CvArr dst)"""
  return _cv.cvMinS(*args)

def cvMaxS(*args):
  """cvMaxS(CvArr src, double value, CvArr dst)"""
  return _cv.cvMaxS(*args)

def cvAbsDiff(*args):
  """cvAbsDiff(CvArr src1, CvArr src2, CvArr dst)"""
  return _cv.cvAbsDiff(*args)

def cvAbsDiffS(*args):
  """cvAbsDiffS(CvArr src, CvArr dst, CvScalar value)"""
  return _cv.cvAbsDiffS(*args)

def cvCartToPolar(*args):
  """
    cvCartToPolar(CvArr x, CvArr y, CvArr magnitude, CvArr angle=None, 
        int angle_in_degrees=0)
    """
  return _cv.cvCartToPolar(*args)

def cvPolarToCart(*args):
  """cvPolarToCart(CvArr magnitude, CvArr angle, CvArr x, CvArr y, int angle_in_degrees=0)"""
  return _cv.cvPolarToCart(*args)

def cvPow(*args):
  """cvPow(CvArr src, CvArr dst, double power)"""
  return _cv.cvPow(*args)

def cvExp(*args):
  """cvExp(CvArr src, CvArr dst)"""
  return _cv.cvExp(*args)

def cvLog(*args):
  """cvLog(CvArr src, CvArr dst)"""
  return _cv.cvLog(*args)

def cvFastArctan(*args):
  """cvFastArctan(float y, float x) -> float"""
  return _cv.cvFastArctan(*args)

def cvCbrt(*args):
  """cvCbrt(float value) -> float"""
  return _cv.cvCbrt(*args)

def cvCheckArr(*args):
  """cvCheckArr(CvArr arr, int flags=0, double min_val=0, double max_val=0) -> int"""
  return _cv.cvCheckArr(*args)

def cvRandArr(*args):
  """
    cvRandArr(CvRNG rng, CvArr arr, int dist_type, CvScalar param1, 
        CvScalar param2)
    """
  return _cv.cvRandArr(*args)

def cvRandShuffle(*args):
  """cvRandShuffle(CvArr mat, CvRNG rng, double iter_factor=1.)"""
  return _cv.cvRandShuffle(*args)

def cvSolveCubic(*args):
  """cvSolveCubic(CvMat coeffs, CvMat roots) -> int"""
  return _cv.cvSolveCubic(*args)

def cvCrossProduct(*args):
  """cvCrossProduct(CvArr src1, CvArr src2, CvArr dst)"""
  return _cv.cvCrossProduct(*args)

def cvGEMM(*args):
  """
    cvGEMM(CvArr src1, CvArr src2, double alpha, CvArr src3, double beta, 
        CvArr dst, int tABC=0)
    """
  return _cv.cvGEMM(*args)

def cvTransform(*args):
  """cvTransform(CvArr src, CvArr dst, CvMat transmat, CvMat shiftvec=None)"""
  return _cv.cvTransform(*args)

def cvPerspectiveTransform(*args):
  """cvPerspectiveTransform(CvArr src, CvArr dst, CvMat mat)"""
  return _cv.cvPerspectiveTransform(*args)

def cvMulTransposed(*args):
  """
    cvMulTransposed(CvArr src, CvArr dst, int order, CvArr delta=None, 
        double scale=1.)
    """
  return _cv.cvMulTransposed(*args)

def cvTranspose(*args):
  """cvTranspose(CvArr src, CvArr dst)"""
  return _cv.cvTranspose(*args)

def cvFlip(*args):
  """cvFlip(CvArr src, CvArr dst=None, int flip_mode=0)"""
  return _cv.cvFlip(*args)

def cvSVD(*args):
  """cvSVD(CvArr A, CvArr W, CvArr U=None, CvArr V=None, int flags=0)"""
  return _cv.cvSVD(*args)

def cvSVBkSb(*args):
  """cvSVBkSb(CvArr W, CvArr U, CvArr V, CvArr B, CvArr X, int flags)"""
  return _cv.cvSVBkSb(*args)

def cvInvert(*args):
  """cvInvert(CvArr src, CvArr dst, int method=0) -> double"""
  return _cv.cvInvert(*args)

def cvSolve(*args):
  """cvSolve(CvArr src1, CvArr src2, CvArr dst, int method=0) -> int"""
  return _cv.cvSolve(*args)

def cvDet(*args):
  """cvDet(CvArr mat) -> double"""
  return _cv.cvDet(*args)

def cvTrace(*args):
  """cvTrace(CvArr mat) -> CvScalar"""
  return _cv.cvTrace(*args)

def cvEigenVV(*args):
  """cvEigenVV(CvArr mat, CvArr evects, CvArr evals, double eps=0)"""
  return _cv.cvEigenVV(*args)

def cvSetIdentity(*args):
  """cvSetIdentity(CvArr mat, CvScalar value=cvRealScalar(1))"""
  return _cv.cvSetIdentity(*args)

def cvRange(*args):
  """cvRange(CvArr mat, double start, double end) -> CvArr"""
  return _cv.cvRange(*args)

def cvCalcCovarMatrix(*args):
  """cvCalcCovarMatrix(CvArr vects, int count, CvArr cov_mat, CvArr avg, int flags)"""
  return _cv.cvCalcCovarMatrix(*args)

def cvCalcPCA(*args):
  """
    cvCalcPCA(CvArr data, CvArr mean, CvArr eigenvals, CvArr eigenvects, 
        int flags)
    """
  return _cv.cvCalcPCA(*args)

def cvProjectPCA(*args):
  """cvProjectPCA(CvArr data, CvArr mean, CvArr eigenvects, CvArr result)"""
  return _cv.cvProjectPCA(*args)

def cvBackProjectPCA(*args):
  """cvBackProjectPCA(CvArr proj, CvArr mean, CvArr eigenvects, CvArr result)"""
  return _cv.cvBackProjectPCA(*args)

def cvMahalanobis(*args):
  """cvMahalanobis(CvArr vec1, CvArr vec2, CvArr mat) -> double"""
  return _cv.cvMahalanobis(*args)

def cvSum(*args):
  """cvSum(CvArr arr) -> CvScalar"""
  return _cv.cvSum(*args)

def cvCountNonZero(*args):
  """cvCountNonZero(CvArr arr) -> int"""
  return _cv.cvCountNonZero(*args)

def cvAvg(*args):
  """cvAvg(CvArr arr, CvArr mask=None) -> CvScalar"""
  return _cv.cvAvg(*args)

def cvAvgSdv(*args):
  """cvAvgSdv(CvArr arr, CvScalar mean, CvScalar std_dev, CvArr mask=None)"""
  return _cv.cvAvgSdv(*args)

def cvMinMaxLoc(*args):
  """
    cvMinMaxLoc(CvArr arr, double min_val, double max_val, CvPoint min_loc=None, 
        CvPoint max_loc=None, CvArr mask=None)
    """
  return _cv.cvMinMaxLoc(*args)

def cvNorm(*args):
  """cvNorm(CvArr arr1, CvArr arr2=None, int norm_type=4, CvArr mask=None) -> double"""
  return _cv.cvNorm(*args)

def cvNormalize(*args):
  """
    cvNormalize(CvArr src, CvArr dst, double a=1., double b=0., int norm_type=4, 
        CvArr mask=None)
    """
  return _cv.cvNormalize(*args)

def cvReduce(*args):
  """cvReduce(CvArr src, CvArr dst, int dim=-1, int op=0)"""
  return _cv.cvReduce(*args)

def cvDFT(*args):
  """cvDFT(CvArr src, CvArr dst, int flags, int nonzero_rows=0)"""
  return _cv.cvDFT(*args)

def cvMulSpectrums(*args):
  """cvMulSpectrums(CvArr src1, CvArr src2, CvArr dst, int flags)"""
  return _cv.cvMulSpectrums(*args)

def cvGetOptimalDFTSize(*args):
  """cvGetOptimalDFTSize(int size0) -> int"""
  return _cv.cvGetOptimalDFTSize(*args)

def cvDCT(*args):
  """cvDCT(CvArr src, CvArr dst, int flags)"""
  return _cv.cvDCT(*args)

def cvSliceLength(*args):
  """cvSliceLength(CvSlice slice, CvSeq seq) -> int"""
  return _cv.cvSliceLength(*args)

def cvCreateMemStorage(*args):
  """cvCreateMemStorage(int block_size=0) -> CvMemStorage"""
  return _cv.cvCreateMemStorage(*args)

def cvCreateChildMemStorage(*args):
  """cvCreateChildMemStorage(CvMemStorage parent) -> CvMemStorage"""
  return _cv.cvCreateChildMemStorage(*args)

def cvClearMemStorage(*args):
  """cvClearMemStorage(CvMemStorage storage)"""
  return _cv.cvClearMemStorage(*args)

def cvSaveMemStoragePos(*args):
  """cvSaveMemStoragePos(CvMemStorage storage, CvMemStoragePos pos)"""
  return _cv.cvSaveMemStoragePos(*args)

def cvRestoreMemStoragePos(*args):
  """cvRestoreMemStoragePos(CvMemStorage storage, CvMemStoragePos pos)"""
  return _cv.cvRestoreMemStoragePos(*args)

def cvMemStorageAlloc(*args):
  """cvMemStorageAlloc(CvMemStorage storage, size_t size) -> void"""
  return _cv.cvMemStorageAlloc(*args)

def cvMemStorageAllocString(*args):
  """cvMemStorageAllocString(CvMemStorage storage, char ptr, int len=-1) -> CvString"""
  return _cv.cvMemStorageAllocString(*args)

def cvCreateSeq(*args):
  """cvCreateSeq(int seq_flags, int header_size, int elem_size, CvMemStorage storage) -> CvSeq"""
  return _cv.cvCreateSeq(*args)

def cvSetSeqBlockSize(*args):
  """cvSetSeqBlockSize(CvSeq seq, int delta_elems)"""
  return _cv.cvSetSeqBlockSize(*args)

def cvSeqPush(*args):
  """cvSeqPush(CvSeq seq, void element=None) -> char"""
  return _cv.cvSeqPush(*args)

def cvSeqPushFront(*args):
  """cvSeqPushFront(CvSeq seq, void element=None) -> char"""
  return _cv.cvSeqPushFront(*args)

def cvSeqPop(*args):
  """cvSeqPop(CvSeq seq, void element=None)"""
  return _cv.cvSeqPop(*args)

def cvSeqPopFront(*args):
  """cvSeqPopFront(CvSeq seq, void element=None)"""
  return _cv.cvSeqPopFront(*args)

def cvSeqPushMulti(*args):
  """cvSeqPushMulti(CvSeq seq, void elements, int count, int in_front=0)"""
  return _cv.cvSeqPushMulti(*args)

def cvSeqPopMulti(*args):
  """cvSeqPopMulti(CvSeq seq, void elements, int count, int in_front=0)"""
  return _cv.cvSeqPopMulti(*args)

def cvSeqInsert(*args):
  """cvSeqInsert(CvSeq seq, int before_index, void element=None) -> char"""
  return _cv.cvSeqInsert(*args)

def cvSeqRemove(*args):
  """cvSeqRemove(CvSeq seq, int index)"""
  return _cv.cvSeqRemove(*args)

def cvClearSeq(*args):
  """cvClearSeq(CvSeq seq)"""
  return _cv.cvClearSeq(*args)

def cvGetSeqElem(*args):
  """cvGetSeqElem(CvSeq seq, int index) -> char"""
  return _cv.cvGetSeqElem(*args)

def cvSeqElemIdx(*args):
  """cvSeqElemIdx(CvSeq seq, void element, CvSeqBlock block=None) -> int"""
  return _cv.cvSeqElemIdx(*args)

def cvStartAppendToSeq(*args):
  """cvStartAppendToSeq(CvSeq seq, CvSeqWriter writer)"""
  return _cv.cvStartAppendToSeq(*args)

def cvStartWriteSeq(*args):
  """
    cvStartWriteSeq(int seq_flags, int header_size, int elem_size, CvMemStorage storage, 
        CvSeqWriter writer)
    """
  return _cv.cvStartWriteSeq(*args)

def cvEndWriteSeq(*args):
  """cvEndWriteSeq(CvSeqWriter writer) -> CvSeq"""
  return _cv.cvEndWriteSeq(*args)

def cvFlushSeqWriter(*args):
  """cvFlushSeqWriter(CvSeqWriter writer)"""
  return _cv.cvFlushSeqWriter(*args)

def cvStartReadSeq(*args):
  """cvStartReadSeq(CvSeq seq, CvSeqReader reader, int reverse=0)"""
  return _cv.cvStartReadSeq(*args)

def cvGetSeqReaderPos(*args):
  """cvGetSeqReaderPos(CvSeqReader reader) -> int"""
  return _cv.cvGetSeqReaderPos(*args)

def cvSetSeqReaderPos(*args):
  """cvSetSeqReaderPos(CvSeqReader reader, int index, int is_relative=0)"""
  return _cv.cvSetSeqReaderPos(*args)

def cvMakeSeqHeaderForArray(*args):
  """
    cvMakeSeqHeaderForArray(int seq_type, int header_size, int elem_size, void elements, 
        int total, CvSeq seq, CvSeqBlock block) -> CvSeq
    """
  return _cv.cvMakeSeqHeaderForArray(*args)

def cvSeqSlice(*args):
  """
    cvSeqSlice(CvSeq seq, CvSlice slice, CvMemStorage storage=None, 
        int copy_data=0) -> CvSeq
    """
  return _cv.cvSeqSlice(*args)

def cvCloneSeq(*args):
  """cvCloneSeq(CvSeq seq, CvMemStorage storage=None) -> CvSeq"""
  return _cv.cvCloneSeq(*args)

def cvSeqRemoveSlice(*args):
  """cvSeqRemoveSlice(CvSeq seq, CvSlice slice)"""
  return _cv.cvSeqRemoveSlice(*args)

def cvSeqInsertSlice(*args):
  """cvSeqInsertSlice(CvSeq seq, int before_index, CvArr from_arr)"""
  return _cv.cvSeqInsertSlice(*args)

def cvSeqSort(*args):
  """cvSeqSort(CvSeq seq, CvCmpFunc func, void userdata=None)"""
  return _cv.cvSeqSort(*args)

def cvSeqSearch(*args):
  """
    cvSeqSearch(CvSeq seq, void elem, CvCmpFunc func, int is_sorted, 
        int elem_idx, void userdata=None) -> char
    """
  return _cv.cvSeqSearch(*args)

def cvSeqInvert(*args):
  """cvSeqInvert(CvSeq seq)"""
  return _cv.cvSeqInvert(*args)

def cvSeqPartition(*args):
  """
    cvSeqPartition(CvSeq seq, CvMemStorage storage, CvSeq labels, CvCmpFunc is_equal, 
        void userdata) -> int
    """
  return _cv.cvSeqPartition(*args)

def cvChangeSeqBlock(*args):
  """cvChangeSeqBlock(void reader, int direction)"""
  return _cv.cvChangeSeqBlock(*args)

def cvCreateSeqBlock(*args):
  """cvCreateSeqBlock(CvSeqWriter writer)"""
  return _cv.cvCreateSeqBlock(*args)

def cvCreateSet(*args):
  """cvCreateSet(int set_flags, int header_size, int elem_size, CvMemStorage storage) -> CvSet"""
  return _cv.cvCreateSet(*args)

def cvSetAdd(*args):
  """cvSetAdd(CvSet set_header, CvSetElem elem=None, CvSetElem inserted_elem=None) -> int"""
  return _cv.cvSetAdd(*args)

def cvSetNew(*args):
  """cvSetNew(CvSet set_header) -> CvSetElem"""
  return _cv.cvSetNew(*args)

def cvSetRemoveByPtr(*args):
  """cvSetRemoveByPtr(CvSet set_header, void elem)"""
  return _cv.cvSetRemoveByPtr(*args)

def cvSetRemove(*args):
  """cvSetRemove(CvSet set_header, int index)"""
  return _cv.cvSetRemove(*args)

def cvGetSetElem(*args):
  """cvGetSetElem(CvSet set_header, int index) -> CvSetElem"""
  return _cv.cvGetSetElem(*args)

def cvClearSet(*args):
  """cvClearSet(CvSet set_header)"""
  return _cv.cvClearSet(*args)

def cvCreateGraph(*args):
  """
    cvCreateGraph(int graph_flags, int header_size, int vtx_size, int edge_size, 
        CvMemStorage storage) -> CvGraph
    """
  return _cv.cvCreateGraph(*args)

def cvGraphAddVtx(*args):
  """cvGraphAddVtx(CvGraph graph, CvGraphVtx vtx=None, CvGraphVtx inserted_vtx=None) -> int"""
  return _cv.cvGraphAddVtx(*args)

def cvGraphRemoveVtx(*args):
  """cvGraphRemoveVtx(CvGraph graph, int index) -> int"""
  return _cv.cvGraphRemoveVtx(*args)

def cvGraphRemoveVtxByPtr(*args):
  """cvGraphRemoveVtxByPtr(CvGraph graph, CvGraphVtx vtx) -> int"""
  return _cv.cvGraphRemoveVtxByPtr(*args)

def cvGraphAddEdge(*args):
  """
    cvGraphAddEdge(CvGraph graph, int start_idx, int end_idx, CvGraphEdge edge=None, 
        CvGraphEdge inserted_edge=None) -> int
    """
  return _cv.cvGraphAddEdge(*args)

def cvGraphAddEdgeByPtr(*args):
  """
    cvGraphAddEdgeByPtr(CvGraph graph, CvGraphVtx start_vtx, CvGraphVtx end_vtx, 
        CvGraphEdge edge=None, CvGraphEdge inserted_edge=None) -> int
    """
  return _cv.cvGraphAddEdgeByPtr(*args)

def cvGraphRemoveEdge(*args):
  """cvGraphRemoveEdge(CvGraph graph, int start_idx, int end_idx)"""
  return _cv.cvGraphRemoveEdge(*args)

def cvGraphRemoveEdgeByPtr(*args):
  """cvGraphRemoveEdgeByPtr(CvGraph graph, CvGraphVtx start_vtx, CvGraphVtx end_vtx)"""
  return _cv.cvGraphRemoveEdgeByPtr(*args)

def cvFindGraphEdge(*args):
  """cvFindGraphEdge(CvGraph graph, int start_idx, int end_idx) -> CvGraphEdge"""
  return _cv.cvFindGraphEdge(*args)

def cvFindGraphEdgeByPtr(*args):
  """cvFindGraphEdgeByPtr(CvGraph graph, CvGraphVtx start_vtx, CvGraphVtx end_vtx) -> CvGraphEdge"""
  return _cv.cvFindGraphEdgeByPtr(*args)

def cvClearGraph(*args):
  """cvClearGraph(CvGraph graph)"""
  return _cv.cvClearGraph(*args)

def cvGraphVtxDegree(*args):
  """cvGraphVtxDegree(CvGraph graph, int vtx_idx) -> int"""
  return _cv.cvGraphVtxDegree(*args)

def cvGraphVtxDegreeByPtr(*args):
  """cvGraphVtxDegreeByPtr(CvGraph graph, CvGraphVtx vtx) -> int"""
  return _cv.cvGraphVtxDegreeByPtr(*args)
class CvGraphScanner(_object):
    """Proxy of C++ CvGraphScanner class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvGraphScanner, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvGraphScanner, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["vtx"] = _cv.CvGraphScanner_vtx_set
    __swig_getmethods__["vtx"] = _cv.CvGraphScanner_vtx_get
    if _newclass:vtx = _swig_property(_cv.CvGraphScanner_vtx_get, _cv.CvGraphScanner_vtx_set)
    __swig_setmethods__["dst"] = _cv.CvGraphScanner_dst_set
    __swig_getmethods__["dst"] = _cv.CvGraphScanner_dst_get
    if _newclass:dst = _swig_property(_cv.CvGraphScanner_dst_get, _cv.CvGraphScanner_dst_set)
    __swig_setmethods__["edge"] = _cv.CvGraphScanner_edge_set
    __swig_getmethods__["edge"] = _cv.CvGraphScanner_edge_get
    if _newclass:edge = _swig_property(_cv.CvGraphScanner_edge_get, _cv.CvGraphScanner_edge_set)
    __swig_setmethods__["graph"] = _cv.CvGraphScanner_graph_set
    __swig_getmethods__["graph"] = _cv.CvGraphScanner_graph_get
    if _newclass:graph = _swig_property(_cv.CvGraphScanner_graph_get, _cv.CvGraphScanner_graph_set)
    __swig_setmethods__["stack"] = _cv.CvGraphScanner_stack_set
    __swig_getmethods__["stack"] = _cv.CvGraphScanner_stack_get
    if _newclass:stack = _swig_property(_cv.CvGraphScanner_stack_get, _cv.CvGraphScanner_stack_set)
    __swig_setmethods__["index"] = _cv.CvGraphScanner_index_set
    __swig_getmethods__["index"] = _cv.CvGraphScanner_index_get
    if _newclass:index = _swig_property(_cv.CvGraphScanner_index_get, _cv.CvGraphScanner_index_set)
    __swig_setmethods__["mask"] = _cv.CvGraphScanner_mask_set
    __swig_getmethods__["mask"] = _cv.CvGraphScanner_mask_get
    if _newclass:mask = _swig_property(_cv.CvGraphScanner_mask_get, _cv.CvGraphScanner_mask_set)
    __swig_destroy__ = _cv.delete_CvGraphScanner
    __del__ = lambda self : None;
CvGraphScanner_swigregister = _cv.CvGraphScanner_swigregister
CvGraphScanner_swigregister(CvGraphScanner)


def cvCreateGraphScanner(*args):
  """cvCreateGraphScanner(CvGraph graph, CvGraphVtx vtx=None, int mask=-1) -> CvGraphScanner"""
  return _cv.cvCreateGraphScanner(*args)

def cvNextGraphItem(*args):
  """cvNextGraphItem(CvGraphScanner scanner) -> int"""
  return _cv.cvNextGraphItem(*args)

def cvCloneGraph(*args):
  """cvCloneGraph(CvGraph graph, CvMemStorage storage) -> CvGraph"""
  return _cv.cvCloneGraph(*args)

def cvLine(*args):
  """
    cvLine(CvArr img, CvPoint pt1, CvPoint pt2, CvScalar color, 
        int thickness=1, int line_type=8, int shift=0)
    """
  return _cv.cvLine(*args)

def cvRectangle(*args):
  """
    cvRectangle(CvArr img, CvPoint pt1, CvPoint pt2, CvScalar color, 
        int thickness=1, int line_type=8, int shift=0)
    """
  return _cv.cvRectangle(*args)

def cvCircle(*args):
  """
    cvCircle(CvArr img, CvPoint center, int radius, CvScalar color, 
        int thickness=1, int line_type=8, int shift=0)
    """
  return _cv.cvCircle(*args)

def cvEllipse(*args):
  """
    cvEllipse(CvArr img, CvPoint center, CvSize axes, double angle, 
        double start_angle, double end_angle, CvScalar color, 
        int thickness=1, int line_type=8, 
        int shift=0)
    """
  return _cv.cvEllipse(*args)

def cvEllipseBox(*args):
  """
    cvEllipseBox(CvArr img, CvBox2D box, CvScalar color, int thickness=1, 
        int line_type=8, int shift=0)
    """
  return _cv.cvEllipseBox(*args)

def cvFillConvexPoly(*args):
  """
    cvFillConvexPoly(CvArr img, CvPoint pts, CvScalar color, int line_type=8, 
        int shift=0)
    """
  return _cv.cvFillConvexPoly(*args)

def cvFillPoly(*args):
  """
    cvFillPoly(CvArr img, CvPoint pts, CvScalar color, int line_type=8, 
        int shift=0)
    """
  return _cv.cvFillPoly(*args)

def cvPolyLine(*args):
  """
    cvPolyLine(CvArr img, CvPoint pts, int is_closed, CvScalar color, 
        int thickness=1, int line_type=8, int shift=0)
    """
  return _cv.cvPolyLine(*args)

def cvClipLine(*args):
  """cvClipLine(CvSize img_size, CvPoint pt1, CvPoint pt2) -> int"""
  return _cv.cvClipLine(*args)

def cvInitLineIterator(*args):
  """
    cvInitLineIterator(CvArr image, CvPoint pt1, CvPoint pt2, CvLineIterator line_iterator, 
        int connectivity=8, int left_to_right=0) -> int
    """
  return _cv.cvInitLineIterator(*args)
class CvFont(_object):
    """Proxy of C++ CvFont class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvFont, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvFont, name)
    __repr__ = _swig_repr
    __swig_setmethods__["font_face"] = _cv.CvFont_font_face_set
    __swig_getmethods__["font_face"] = _cv.CvFont_font_face_get
    if _newclass:font_face = _swig_property(_cv.CvFont_font_face_get, _cv.CvFont_font_face_set)
    __swig_setmethods__["ascii"] = _cv.CvFont_ascii_set
    __swig_getmethods__["ascii"] = _cv.CvFont_ascii_get
    if _newclass:ascii = _swig_property(_cv.CvFont_ascii_get, _cv.CvFont_ascii_set)
    __swig_setmethods__["greek"] = _cv.CvFont_greek_set
    __swig_getmethods__["greek"] = _cv.CvFont_greek_get
    if _newclass:greek = _swig_property(_cv.CvFont_greek_get, _cv.CvFont_greek_set)
    __swig_setmethods__["cyrillic"] = _cv.CvFont_cyrillic_set
    __swig_getmethods__["cyrillic"] = _cv.CvFont_cyrillic_get
    if _newclass:cyrillic = _swig_property(_cv.CvFont_cyrillic_get, _cv.CvFont_cyrillic_set)
    __swig_setmethods__["hscale"] = _cv.CvFont_hscale_set
    __swig_getmethods__["hscale"] = _cv.CvFont_hscale_get
    if _newclass:hscale = _swig_property(_cv.CvFont_hscale_get, _cv.CvFont_hscale_set)
    __swig_setmethods__["vscale"] = _cv.CvFont_vscale_set
    __swig_getmethods__["vscale"] = _cv.CvFont_vscale_get
    if _newclass:vscale = _swig_property(_cv.CvFont_vscale_get, _cv.CvFont_vscale_set)
    __swig_setmethods__["shear"] = _cv.CvFont_shear_set
    __swig_getmethods__["shear"] = _cv.CvFont_shear_get
    if _newclass:shear = _swig_property(_cv.CvFont_shear_get, _cv.CvFont_shear_set)
    __swig_setmethods__["thickness"] = _cv.CvFont_thickness_set
    __swig_getmethods__["thickness"] = _cv.CvFont_thickness_get
    if _newclass:thickness = _swig_property(_cv.CvFont_thickness_get, _cv.CvFont_thickness_set)
    __swig_setmethods__["dx"] = _cv.CvFont_dx_set
    __swig_getmethods__["dx"] = _cv.CvFont_dx_get
    if _newclass:dx = _swig_property(_cv.CvFont_dx_get, _cv.CvFont_dx_set)
    __swig_setmethods__["line_type"] = _cv.CvFont_line_type_set
    __swig_getmethods__["line_type"] = _cv.CvFont_line_type_get
    if _newclass:line_type = _swig_property(_cv.CvFont_line_type_get, _cv.CvFont_line_type_set)
    def __init__(self, *args): 
        """__init__(self) -> CvFont"""
        this = _cv.new_CvFont(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvFont
    __del__ = lambda self : None;
CvFont_swigregister = _cv.CvFont_swigregister
CvFont_swigregister(CvFont)


def cvInitFont(*args):
  """
    cvInitFont(CvFont font, double hscale, double vscale, double shear=0, 
        int thickness=1, int line_type=8)
    """
  return _cv.cvInitFont(*args)

def cvFont(*args):
  """cvFont(double scale, int thickness=1) -> CvFont"""
  return _cv.cvFont(*args)

def cvPutText(*args):
  """cvPutText(CvArr img, char text, CvPoint org, CvFont font, CvScalar color)"""
  return _cv.cvPutText(*args)

def cvGetTextSize(*args):
  """cvGetTextSize(char text_string, CvFont font, CvSize text_size)"""
  return _cv.cvGetTextSize(*args)

def cvColorToScalar(*args):
  """cvColorToScalar(double packed_color, int arrtype) -> CvScalar"""
  return _cv.cvColorToScalar(*args)

def cvEllipse2Poly(*args):
  """
    cvEllipse2Poly(CvPoint center, CvSize axes, int angle, int arc_start, 
        int arc_end, CvPoint pts, int delta) -> int
    """
  return _cv.cvEllipse2Poly(*args)

def cvDrawContours(*args):
  """
    cvDrawContours(CvArr img, CvSeq contour, CvScalar external_color, 
        CvScalar hole_color, int max_level, int thickness=1, 
        int line_type=8, CvPoint offset=cvPoint(0,0))
    """
  return _cv.cvDrawContours(*args)

def cvLUT(*args):
  """cvLUT(CvArr src, CvArr dst, CvArr lut)"""
  return _cv.cvLUT(*args)
class CvTreeNodeIterator(_object):
    """Proxy of C++ CvTreeNodeIterator class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvTreeNodeIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvTreeNodeIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["node"] = _cv.CvTreeNodeIterator_node_set
    __swig_getmethods__["node"] = _cv.CvTreeNodeIterator_node_get
    if _newclass:node = _swig_property(_cv.CvTreeNodeIterator_node_get, _cv.CvTreeNodeIterator_node_set)
    __swig_setmethods__["level"] = _cv.CvTreeNodeIterator_level_set
    __swig_getmethods__["level"] = _cv.CvTreeNodeIterator_level_get
    if _newclass:level = _swig_property(_cv.CvTreeNodeIterator_level_get, _cv.CvTreeNodeIterator_level_set)
    __swig_setmethods__["max_level"] = _cv.CvTreeNodeIterator_max_level_set
    __swig_getmethods__["max_level"] = _cv.CvTreeNodeIterator_max_level_get
    if _newclass:max_level = _swig_property(_cv.CvTreeNodeIterator_max_level_get, _cv.CvTreeNodeIterator_max_level_set)
    def __init__(self, *args): 
        """__init__(self) -> CvTreeNodeIterator"""
        this = _cv.new_CvTreeNodeIterator(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvTreeNodeIterator
    __del__ = lambda self : None;
CvTreeNodeIterator_swigregister = _cv.CvTreeNodeIterator_swigregister
CvTreeNodeIterator_swigregister(CvTreeNodeIterator)


def cvInitTreeNodeIterator(*args):
  """cvInitTreeNodeIterator(CvTreeNodeIterator tree_iterator, void first, int max_level)"""
  return _cv.cvInitTreeNodeIterator(*args)

def cvNextTreeNode(*args):
  """cvNextTreeNode(CvTreeNodeIterator tree_iterator) -> void"""
  return _cv.cvNextTreeNode(*args)

def cvPrevTreeNode(*args):
  """cvPrevTreeNode(CvTreeNodeIterator tree_iterator) -> void"""
  return _cv.cvPrevTreeNode(*args)

def cvInsertNodeIntoTree(*args):
  """cvInsertNodeIntoTree(void node, void parent, void frame)"""
  return _cv.cvInsertNodeIntoTree(*args)

def cvRemoveNodeFromTree(*args):
  """cvRemoveNodeFromTree(void node, void frame)"""
  return _cv.cvRemoveNodeFromTree(*args)

def cvTreeToNodeSeq(*args):
  """cvTreeToNodeSeq(void first, int header_size, CvMemStorage storage) -> CvSeq"""
  return _cv.cvTreeToNodeSeq(*args)

def cvKMeans2(*args):
  """cvKMeans2(CvArr samples, int cluster_count, CvArr labels, CvTermCriteria termcrit)"""
  return _cv.cvKMeans2(*args)

def cvRegisterModule(*args):
  """cvRegisterModule(CvModuleInfo module_info) -> int"""
  return _cv.cvRegisterModule(*args)

def cvUseOptimized(*args):
  """cvUseOptimized(int on_off) -> int"""
  return _cv.cvUseOptimized(*args)

def cvGetModuleInfo(*args):
  """cvGetModuleInfo(char module_name, char version, char loaded_addon_plugins)"""
  return _cv.cvGetModuleInfo(*args)

def cvGetErrStatus(*args):
  """cvGetErrStatus() -> int"""
  return _cv.cvGetErrStatus(*args)

def cvSetErrStatus(*args):
  """cvSetErrStatus(int status)"""
  return _cv.cvSetErrStatus(*args)

def cvGetErrMode(*args):
  """cvGetErrMode() -> int"""
  return _cv.cvGetErrMode(*args)

def cvSetErrMode(*args):
  """cvSetErrMode(int mode) -> int"""
  return _cv.cvSetErrMode(*args)

def cvError(*args):
  """
    cvError(int status, char func_name, char err_msg, char file_name, 
        int line)
    """
  return _cv.cvError(*args)

def cvErrorStr(*args):
  """cvErrorStr(int status) -> char"""
  return _cv.cvErrorStr(*args)

def cvGetErrInfo(*args):
  """
    cvGetErrInfo(char errcode_desc, char description, char filename, 
        int line) -> int
    """
  return _cv.cvGetErrInfo(*args)

def cvErrorFromIppStatus(*args):
  """cvErrorFromIppStatus(int ipp_status) -> int"""
  return _cv.cvErrorFromIppStatus(*args)

def cvRedirectError(*args):
  """
    cvRedirectError(CvErrorCallback error_handler, void userdata=None, 
        void prev_userdata=None) -> CvErrorCallback
    """
  return _cv.cvRedirectError(*args)

def cvNulDevReport(*args):
  """
    cvNulDevReport(int status, char func_name, char err_msg, char file_name, 
        int line, void userdata) -> int
    """
  return _cv.cvNulDevReport(*args)

def cvStdErrReport(*args):
  """
    cvStdErrReport(int status, char func_name, char err_msg, char file_name, 
        int line, void userdata) -> int
    """
  return _cv.cvStdErrReport(*args)

def cvGuiBoxReport(*args):
  """
    cvGuiBoxReport(int status, char func_name, char err_msg, char file_name, 
        int line, void userdata) -> int
    """
  return _cv.cvGuiBoxReport(*args)

def cvSetMemoryManager(*args):
  """
    cvSetMemoryManager(CvAllocFunc alloc_func=None, CvFreeFunc free_func=None, 
        void userdata=None)
    """
  return _cv.cvSetMemoryManager(*args)

def cvSetIPLAllocators(*args):
  """
    cvSetIPLAllocators(Cv_iplCreateImageHeader create_header, Cv_iplAllocateImageData allocate_data, 
        Cv_iplDeallocate deallocate, 
        Cv_iplCreateROI create_roi, Cv_iplCloneImage clone_image)
    """
  return _cv.cvSetIPLAllocators(*args)

def cvOpenFileStorage(*args):
  """cvOpenFileStorage(char filename, CvMemStorage memstorage, int flags) -> CvFileStorage"""
  return _cv.cvOpenFileStorage(*args)

def cvAttrValue(*args):
  """cvAttrValue(CvAttrList attr, char attr_name) -> char"""
  return _cv.cvAttrValue(*args)

def cvStartWriteStruct(*args):
  """
    cvStartWriteStruct(CvFileStorage fs, char name, int struct_flags, char type_name=None, 
        CvAttrList attributes=cvAttrList())
    """
  return _cv.cvStartWriteStruct(*args)

def cvEndWriteStruct(*args):
  """cvEndWriteStruct(CvFileStorage fs)"""
  return _cv.cvEndWriteStruct(*args)

def cvWriteInt(*args):
  """cvWriteInt(CvFileStorage fs, char name, int value)"""
  return _cv.cvWriteInt(*args)

def cvWriteReal(*args):
  """cvWriteReal(CvFileStorage fs, char name, double value)"""
  return _cv.cvWriteReal(*args)

def cvWriteString(*args):
  """cvWriteString(CvFileStorage fs, char name, char str, int quote=0)"""
  return _cv.cvWriteString(*args)

def cvWriteComment(*args):
  """cvWriteComment(CvFileStorage fs, char comment, int eol_comment)"""
  return _cv.cvWriteComment(*args)

def cvWrite(*args):
  """cvWrite(CvFileStorage fs, char name, void ptr, CvAttrList attributes=cvAttrList())"""
  return _cv.cvWrite(*args)

def cvStartNextStream(*args):
  """cvStartNextStream(CvFileStorage fs)"""
  return _cv.cvStartNextStream(*args)

def cvWriteRawData(*args):
  """cvWriteRawData(CvFileStorage fs, void src, int len, char dt)"""
  return _cv.cvWriteRawData(*args)

def cvGetHashedKey(*args):
  """cvGetHashedKey(CvFileStorage fs, char name, int len=-1, int create_missing=0) -> CvStringHashNode"""
  return _cv.cvGetHashedKey(*args)

def cvGetRootFileNode(*args):
  """cvGetRootFileNode(CvFileStorage fs, int stream_index=0) -> CvFileNode"""
  return _cv.cvGetRootFileNode(*args)

def cvGetFileNode(*args):
  """
    cvGetFileNode(CvFileStorage fs, CvFileNode map, CvStringHashNode key, 
        int create_missing=0) -> CvFileNode
    """
  return _cv.cvGetFileNode(*args)

def cvGetFileNodeByName(*args):
  """cvGetFileNodeByName(CvFileStorage fs, CvFileNode map, char name) -> CvFileNode"""
  return _cv.cvGetFileNodeByName(*args)

def cvReadInt(*args):
  """cvReadInt(CvFileNode node, int default_value=0) -> int"""
  return _cv.cvReadInt(*args)

def cvReadIntByName(*args):
  """cvReadIntByName(CvFileStorage fs, CvFileNode map, char name, int default_value=0) -> int"""
  return _cv.cvReadIntByName(*args)

def cvReadReal(*args):
  """cvReadReal(CvFileNode node, double default_value=0.) -> double"""
  return _cv.cvReadReal(*args)

def cvReadRealByName(*args):
  """cvReadRealByName(CvFileStorage fs, CvFileNode map, char name, double default_value=0.) -> double"""
  return _cv.cvReadRealByName(*args)

def cvReadString(*args):
  """cvReadString(CvFileNode node, char default_value=None) -> char"""
  return _cv.cvReadString(*args)

def cvReadStringByName(*args):
  """cvReadStringByName(CvFileStorage fs, CvFileNode map, char name, char default_value=None) -> char"""
  return _cv.cvReadStringByName(*args)

def cvRead(*args):
  """cvRead(CvFileStorage fs, CvFileNode node, CvAttrList attributes=None) -> void"""
  return _cv.cvRead(*args)

def cvReadByName(*args):
  """cvReadByName(CvFileStorage fs, CvFileNode map, char name, CvAttrList attributes=None) -> void"""
  return _cv.cvReadByName(*args)

def cvStartReadRawData(*args):
  """cvStartReadRawData(CvFileStorage fs, CvFileNode src, CvSeqReader reader)"""
  return _cv.cvStartReadRawData(*args)

def cvReadRawDataSlice(*args):
  """
    cvReadRawDataSlice(CvFileStorage fs, CvSeqReader reader, int count, void dst, 
        char dt)
    """
  return _cv.cvReadRawDataSlice(*args)

def cvReadRawData(*args):
  """cvReadRawData(CvFileStorage fs, CvFileNode src, void dst, char dt)"""
  return _cv.cvReadRawData(*args)

def cvWriteFileNode(*args):
  """
    cvWriteFileNode(CvFileStorage fs, char new_node_name, CvFileNode node, 
        int embed)
    """
  return _cv.cvWriteFileNode(*args)

def cvGetFileNodeName(*args):
  """cvGetFileNodeName(CvFileNode node) -> char"""
  return _cv.cvGetFileNodeName(*args)

def cvRegisterType(*args):
  """cvRegisterType(CvTypeInfo info)"""
  return _cv.cvRegisterType(*args)

def cvUnregisterType(*args):
  """cvUnregisterType(char type_name)"""
  return _cv.cvUnregisterType(*args)

def cvFirstType(*args):
  """cvFirstType() -> CvTypeInfo"""
  return _cv.cvFirstType(*args)

def cvFindType(*args):
  """cvFindType(char type_name) -> CvTypeInfo"""
  return _cv.cvFindType(*args)

def cvTypeOf(*args):
  """cvTypeOf(void struct_ptr) -> CvTypeInfo"""
  return _cv.cvTypeOf(*args)

def cvClone(*args):
  """cvClone(void struct_ptr) -> void"""
  return _cv.cvClone(*args)

def cvSave(*args):
  """
    cvSave(char filename, void struct_ptr, char name=None, char comment=None, 
        CvAttrList attributes=cvAttrList())
    """
  return _cv.cvSave(*args)

def cvLoad(*args):
  """
    cvLoad(char filename, CvMemStorage memstorage=None, char name=None, 
        char real_name=None) -> void
    """
  return _cv.cvLoad(*args)

def cvGetTickCount(*args):
  """cvGetTickCount() -> int64"""
  return _cv.cvGetTickCount(*args)

def cvGetTickFrequency(*args):
  """cvGetTickFrequency() -> double"""
  return _cv.cvGetTickFrequency(*args)

def cvGetNumThreads(*args):
  """cvGetNumThreads() -> int"""
  return _cv.cvGetNumThreads(*args)

def cvSetNumThreads(*args):
  """cvSetNumThreads(int threads=0)"""
  return _cv.cvSetNumThreads(*args)

def cvGetThreadNum(*args):
  """cvGetThreadNum() -> int"""
  return _cv.cvGetThreadNum(*args)
class CvImage(_object):
    """Proxy of C++ CvImage class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvImage, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvImage, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvImage
        __init__(self, CvSize size, int depth, int channels) -> CvImage
        __init__(self,  img) -> CvImage
        __init__(self, CvImage img) -> CvImage
        __init__(self, char filename, char imgname=0, int color=-1) -> CvImage
        __init__(self, char filename, char imgname=0) -> CvImage
        __init__(self, char filename) -> CvImage
        __init__(self, CvFileStorage fs, char mapname, char imgname) -> CvImage
        __init__(self, CvFileStorage fs, char seqname, int idx) -> CvImage
        """
        this = _cv.new_CvImage(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvImage
    __del__ = lambda self : None;
    def clone(*args):
        """clone(self) -> CvImage"""
        return _cv.CvImage_clone(*args)

    def create(*args):
        """create(self, CvSize size, int depth, int channels)"""
        return _cv.CvImage_create(*args)

    def release(*args):
        """release(self)"""
        return _cv.CvImage_release(*args)

    def clear(*args):
        """clear(self)"""
        return _cv.CvImage_clear(*args)

    def attach(*args):
        """
        attach(self,  img, bool use_refcount=True)
        attach(self,  img)
        """
        return _cv.CvImage_attach(*args)

    def detach(*args):
        """detach(self)"""
        return _cv.CvImage_detach(*args)

    def load(*args):
        """
        load(self, char filename, char imgname=0, int color=-1) -> bool
        load(self, char filename, char imgname=0) -> bool
        load(self, char filename) -> bool
        """
        return _cv.CvImage_load(*args)

    def read(*args):
        """
        read(self, CvFileStorage fs, char mapname, char imgname) -> bool
        read(self, CvFileStorage fs, char seqname, int idx) -> bool
        """
        return _cv.CvImage_read(*args)

    def save(*args):
        """save(self, char filename, char imgname)"""
        return _cv.CvImage_save(*args)

    def write(*args):
        """write(self, CvFileStorage fs, char imgname)"""
        return _cv.CvImage_write(*args)

    def show(*args):
        """show(self, char window_name)"""
        return _cv.CvImage_show(*args)

    def is_valid(*args):
        """is_valid(self) -> bool"""
        return _cv.CvImage_is_valid(*args)

    def width(*args):
        """width(self) -> int"""
        return _cv.CvImage_width(*args)

    def height(*args):
        """height(self) -> int"""
        return _cv.CvImage_height(*args)

    def size(*args):
        """size(self) -> CvSize"""
        return _cv.CvImage_size(*args)

    def roi_size(*args):
        """roi_size(self) -> CvSize"""
        return _cv.CvImage_roi_size(*args)

    def roi(*args):
        """roi(self) -> CvRect"""
        return _cv.CvImage_roi(*args)

    def coi(*args):
        """coi(self) -> int"""
        return _cv.CvImage_coi(*args)

    def set_roi(*args):
        """set_roi(self, CvRect roi)"""
        return _cv.CvImage_set_roi(*args)

    def reset_roi(*args):
        """reset_roi(self)"""
        return _cv.CvImage_reset_roi(*args)

    def set_coi(*args):
        """set_coi(self, int coi)"""
        return _cv.CvImage_set_coi(*args)

    def depth(*args):
        """depth(self) -> int"""
        return _cv.CvImage_depth(*args)

    def channels(*args):
        """channels(self) -> int"""
        return _cv.CvImage_channels(*args)

    def pix_size(*args):
        """pix_size(self) -> int"""
        return _cv.CvImage_pix_size(*args)

    def data(*args):
        """
        data(self) -> uchar
        data(self) -> uchar
        """
        return _cv.CvImage_data(*args)

    def step(*args):
        """step(self) -> int"""
        return _cv.CvImage_step(*args)

    def origin(*args):
        """origin(self) -> int"""
        return _cv.CvImage_origin(*args)

    def roi_row(*args):
        """
        roi_row(self, int y) -> uchar
        roi_row(self, int y) -> uchar
        """
        return _cv.CvImage_roi_row(*args)

    def asIplImage(*args):
        """asIplImage(self)"""
        return _cv.CvImage_asIplImage(*args)

CvImage_swigregister = _cv.CvImage_swigregister
CvImage_swigregister(CvImage)

class CvMatrix(_object):
    """Proxy of C++ CvMatrix class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMatrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMatrix, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvMatrix
        __init__(self, int rows, int cols, int type) -> CvMatrix
        __init__(self, int rows, int cols, int type, CvMat hdr, void data=0, 
            int step=0x7fffffff) -> CvMatrix
        __init__(self, int rows, int cols, int type, CvMat hdr, void data=0) -> CvMatrix
        __init__(self, int rows, int cols, int type, CvMat hdr) -> CvMatrix
        __init__(self, int rows, int cols, int type, CvMemStorage storage, 
            bool alloc_data=True) -> CvMatrix
        __init__(self, int rows, int cols, int type, CvMemStorage storage) -> CvMatrix
        __init__(self, int rows, int cols, int type, void data, int step=0x7fffffff) -> CvMatrix
        __init__(self, int rows, int cols, int type, void data) -> CvMatrix
        __init__(self, CvMat m) -> CvMatrix
        __init__(self, CvMatrix m) -> CvMatrix
        __init__(self, char filename, char matname=0, int color=-1) -> CvMatrix
        __init__(self, char filename, char matname=0) -> CvMatrix
        __init__(self, char filename) -> CvMatrix
        __init__(self, CvFileStorage fs, char mapname, char matname) -> CvMatrix
        __init__(self, CvFileStorage fs, char seqname, int idx) -> CvMatrix
        """
        this = _cv.new_CvMatrix(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMatrix
    __del__ = lambda self : None;
    def clone(*args):
        """clone(self) -> CvMatrix"""
        return _cv.CvMatrix_clone(*args)

    def set(*args):
        """set(self, CvMat m, bool add_ref)"""
        return _cv.CvMatrix_set(*args)

    def create(*args):
        """create(self, int rows, int cols, int type)"""
        return _cv.CvMatrix_create(*args)

    def addref(*args):
        """addref(self)"""
        return _cv.CvMatrix_addref(*args)

    def release(*args):
        """release(self)"""
        return _cv.CvMatrix_release(*args)

    def clear(*args):
        """clear(self)"""
        return _cv.CvMatrix_clear(*args)

    def load(*args):
        """
        load(self, char filename, char matname=0, int color=-1) -> bool
        load(self, char filename, char matname=0) -> bool
        load(self, char filename) -> bool
        """
        return _cv.CvMatrix_load(*args)

    def read(*args):
        """
        read(self, CvFileStorage fs, char mapname, char matname) -> bool
        read(self, CvFileStorage fs, char seqname, int idx) -> bool
        """
        return _cv.CvMatrix_read(*args)

    def save(*args):
        """save(self, char filename, char matname)"""
        return _cv.CvMatrix_save(*args)

    def write(*args):
        """write(self, CvFileStorage fs, char matname)"""
        return _cv.CvMatrix_write(*args)

    def show(*args):
        """show(self, char window_name)"""
        return _cv.CvMatrix_show(*args)

    def is_valid(*args):
        """is_valid(self) -> bool"""
        return _cv.CvMatrix_is_valid(*args)

    def rows(*args):
        """rows(self) -> int"""
        return _cv.CvMatrix_rows(*args)

    def cols(*args):
        """cols(self) -> int"""
        return _cv.CvMatrix_cols(*args)

    def size(*args):
        """size(self) -> CvSize"""
        return _cv.CvMatrix_size(*args)

    def type(*args):
        """type(self) -> int"""
        return _cv.CvMatrix_type(*args)

    def depth(*args):
        """depth(self) -> int"""
        return _cv.CvMatrix_depth(*args)

    def channels(*args):
        """channels(self) -> int"""
        return _cv.CvMatrix_channels(*args)

    def pix_size(*args):
        """pix_size(self) -> int"""
        return _cv.CvMatrix_pix_size(*args)

    def data(*args):
        """
        data(self) -> uchar
        data(self) -> uchar
        """
        return _cv.CvMatrix_data(*args)

    def step(*args):
        """step(self) -> int"""
        return _cv.CvMatrix_step(*args)

    def set_data(*args):
        """
        set_data(self, void data, int step=0x7fffffff)
        set_data(self, void data)
        """
        return _cv.CvMatrix_set_data(*args)

    def row(*args):
        """
        row(self, int i) -> uchar
        row(self, int i) -> uchar
        """
        return _cv.CvMatrix_row(*args)

    def asCvMat(*args):
        """asCvMat(self) -> CvMat"""
        return _cv.CvMatrix_asCvMat(*args)

CvMatrix_swigregister = _cv.CvMatrix_swigregister
CvMatrix_swigregister(CvMatrix)


def cvSetImageIOFunctions(*args):
  """
    cvSetImageIOFunctions(CvLoadImageFunc _load_image, CvLoadImageMFunc _load_image_m, 
        CvSaveImageFunc _save_image, CvShowImageFunc _show_image) -> int
    """
  return _cv.cvSetImageIOFunctions(*args)
class CvModule(_object):
    """Proxy of C++ CvModule class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvModule, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvModule, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self, CvModuleInfo _info) -> CvModule"""
        this = _cv.new_CvModule(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvModule
    __del__ = lambda self : None;
    __swig_setmethods__["info"] = _cv.CvModule_info_set
    __swig_getmethods__["info"] = _cv.CvModule_info_get
    if _newclass:info = _swig_property(_cv.CvModule_info_get, _cv.CvModule_info_set)
    __swig_setmethods__["first"] = _cv.CvModule_first_set
    __swig_getmethods__["first"] = _cv.CvModule_first_get
    if _newclass:first = _swig_property(_cv.CvModule_first_get, _cv.CvModule_first_set)
    __swig_setmethods__["last"] = _cv.CvModule_last_set
    __swig_getmethods__["last"] = _cv.CvModule_last_get
    if _newclass:last = _swig_property(_cv.CvModule_last_get, _cv.CvModule_last_set)
CvModule_swigregister = _cv.CvModule_swigregister
CvModule_swigregister(CvModule)

class CvType(_object):
    """Proxy of C++ CvType class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvType, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, char type_name, CvIsInstanceFunc is_instance, CvReleaseFunc release=0, 
            CvReadFunc read=0, CvWriteFunc write=0, 
            CvCloneFunc clone=0) -> CvType
        __init__(self, char type_name, CvIsInstanceFunc is_instance, CvReleaseFunc release=0, 
            CvReadFunc read=0, CvWriteFunc write=0) -> CvType
        __init__(self, char type_name, CvIsInstanceFunc is_instance, CvReleaseFunc release=0, 
            CvReadFunc read=0) -> CvType
        __init__(self, char type_name, CvIsInstanceFunc is_instance, CvReleaseFunc release=0) -> CvType
        __init__(self, char type_name, CvIsInstanceFunc is_instance) -> CvType
        """
        this = _cv.new_CvType(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvType
    __del__ = lambda self : None;
    __swig_setmethods__["info"] = _cv.CvType_info_set
    __swig_getmethods__["info"] = _cv.CvType_info_get
    if _newclass:info = _swig_property(_cv.CvType_info_get, _cv.CvType_info_set)
    __swig_setmethods__["first"] = _cv.CvType_first_set
    __swig_getmethods__["first"] = _cv.CvType_first_get
    if _newclass:first = _swig_property(_cv.CvType_first_get, _cv.CvType_first_set)
    __swig_setmethods__["last"] = _cv.CvType_last_set
    __swig_getmethods__["last"] = _cv.CvType_last_get
    if _newclass:last = _swig_property(_cv.CvType_last_get, _cv.CvType_last_set)
CvType_swigregister = _cv.CvType_swigregister
CvType_swigregister(CvType)

class CvMoments(_object):
    """Proxy of C++ CvMoments class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMoments, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMoments, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m00"] = _cv.CvMoments_m00_set
    __swig_getmethods__["m00"] = _cv.CvMoments_m00_get
    if _newclass:m00 = _swig_property(_cv.CvMoments_m00_get, _cv.CvMoments_m00_set)
    __swig_setmethods__["m10"] = _cv.CvMoments_m10_set
    __swig_getmethods__["m10"] = _cv.CvMoments_m10_get
    if _newclass:m10 = _swig_property(_cv.CvMoments_m10_get, _cv.CvMoments_m10_set)
    __swig_setmethods__["m01"] = _cv.CvMoments_m01_set
    __swig_getmethods__["m01"] = _cv.CvMoments_m01_get
    if _newclass:m01 = _swig_property(_cv.CvMoments_m01_get, _cv.CvMoments_m01_set)
    __swig_setmethods__["m20"] = _cv.CvMoments_m20_set
    __swig_getmethods__["m20"] = _cv.CvMoments_m20_get
    if _newclass:m20 = _swig_property(_cv.CvMoments_m20_get, _cv.CvMoments_m20_set)
    __swig_setmethods__["m11"] = _cv.CvMoments_m11_set
    __swig_getmethods__["m11"] = _cv.CvMoments_m11_get
    if _newclass:m11 = _swig_property(_cv.CvMoments_m11_get, _cv.CvMoments_m11_set)
    __swig_setmethods__["m02"] = _cv.CvMoments_m02_set
    __swig_getmethods__["m02"] = _cv.CvMoments_m02_get
    if _newclass:m02 = _swig_property(_cv.CvMoments_m02_get, _cv.CvMoments_m02_set)
    __swig_setmethods__["m30"] = _cv.CvMoments_m30_set
    __swig_getmethods__["m30"] = _cv.CvMoments_m30_get
    if _newclass:m30 = _swig_property(_cv.CvMoments_m30_get, _cv.CvMoments_m30_set)
    __swig_setmethods__["m21"] = _cv.CvMoments_m21_set
    __swig_getmethods__["m21"] = _cv.CvMoments_m21_get
    if _newclass:m21 = _swig_property(_cv.CvMoments_m21_get, _cv.CvMoments_m21_set)
    __swig_setmethods__["m12"] = _cv.CvMoments_m12_set
    __swig_getmethods__["m12"] = _cv.CvMoments_m12_get
    if _newclass:m12 = _swig_property(_cv.CvMoments_m12_get, _cv.CvMoments_m12_set)
    __swig_setmethods__["m03"] = _cv.CvMoments_m03_set
    __swig_getmethods__["m03"] = _cv.CvMoments_m03_get
    if _newclass:m03 = _swig_property(_cv.CvMoments_m03_get, _cv.CvMoments_m03_set)
    __swig_setmethods__["mu20"] = _cv.CvMoments_mu20_set
    __swig_getmethods__["mu20"] = _cv.CvMoments_mu20_get
    if _newclass:mu20 = _swig_property(_cv.CvMoments_mu20_get, _cv.CvMoments_mu20_set)
    __swig_setmethods__["mu11"] = _cv.CvMoments_mu11_set
    __swig_getmethods__["mu11"] = _cv.CvMoments_mu11_get
    if _newclass:mu11 = _swig_property(_cv.CvMoments_mu11_get, _cv.CvMoments_mu11_set)
    __swig_setmethods__["mu02"] = _cv.CvMoments_mu02_set
    __swig_getmethods__["mu02"] = _cv.CvMoments_mu02_get
    if _newclass:mu02 = _swig_property(_cv.CvMoments_mu02_get, _cv.CvMoments_mu02_set)
    __swig_setmethods__["mu30"] = _cv.CvMoments_mu30_set
    __swig_getmethods__["mu30"] = _cv.CvMoments_mu30_get
    if _newclass:mu30 = _swig_property(_cv.CvMoments_mu30_get, _cv.CvMoments_mu30_set)
    __swig_setmethods__["mu21"] = _cv.CvMoments_mu21_set
    __swig_getmethods__["mu21"] = _cv.CvMoments_mu21_get
    if _newclass:mu21 = _swig_property(_cv.CvMoments_mu21_get, _cv.CvMoments_mu21_set)
    __swig_setmethods__["mu12"] = _cv.CvMoments_mu12_set
    __swig_getmethods__["mu12"] = _cv.CvMoments_mu12_get
    if _newclass:mu12 = _swig_property(_cv.CvMoments_mu12_get, _cv.CvMoments_mu12_set)
    __swig_setmethods__["mu03"] = _cv.CvMoments_mu03_set
    __swig_getmethods__["mu03"] = _cv.CvMoments_mu03_get
    if _newclass:mu03 = _swig_property(_cv.CvMoments_mu03_get, _cv.CvMoments_mu03_set)
    __swig_setmethods__["inv_sqrt_m00"] = _cv.CvMoments_inv_sqrt_m00_set
    __swig_getmethods__["inv_sqrt_m00"] = _cv.CvMoments_inv_sqrt_m00_get
    if _newclass:inv_sqrt_m00 = _swig_property(_cv.CvMoments_inv_sqrt_m00_get, _cv.CvMoments_inv_sqrt_m00_set)
    def __init__(self, *args): 
        """__init__(self) -> CvMoments"""
        this = _cv.new_CvMoments(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMoments
    __del__ = lambda self : None;
CvMoments_swigregister = _cv.CvMoments_swigregister
CvMoments_swigregister(CvMoments)

class CvHuMoments(_object):
    """Proxy of C++ CvHuMoments class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvHuMoments, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvHuMoments, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hu1"] = _cv.CvHuMoments_hu1_set
    __swig_getmethods__["hu1"] = _cv.CvHuMoments_hu1_get
    if _newclass:hu1 = _swig_property(_cv.CvHuMoments_hu1_get, _cv.CvHuMoments_hu1_set)
    __swig_setmethods__["hu2"] = _cv.CvHuMoments_hu2_set
    __swig_getmethods__["hu2"] = _cv.CvHuMoments_hu2_get
    if _newclass:hu2 = _swig_property(_cv.CvHuMoments_hu2_get, _cv.CvHuMoments_hu2_set)
    __swig_setmethods__["hu3"] = _cv.CvHuMoments_hu3_set
    __swig_getmethods__["hu3"] = _cv.CvHuMoments_hu3_get
    if _newclass:hu3 = _swig_property(_cv.CvHuMoments_hu3_get, _cv.CvHuMoments_hu3_set)
    __swig_setmethods__["hu4"] = _cv.CvHuMoments_hu4_set
    __swig_getmethods__["hu4"] = _cv.CvHuMoments_hu4_get
    if _newclass:hu4 = _swig_property(_cv.CvHuMoments_hu4_get, _cv.CvHuMoments_hu4_set)
    __swig_setmethods__["hu5"] = _cv.CvHuMoments_hu5_set
    __swig_getmethods__["hu5"] = _cv.CvHuMoments_hu5_get
    if _newclass:hu5 = _swig_property(_cv.CvHuMoments_hu5_get, _cv.CvHuMoments_hu5_set)
    __swig_setmethods__["hu6"] = _cv.CvHuMoments_hu6_set
    __swig_getmethods__["hu6"] = _cv.CvHuMoments_hu6_get
    if _newclass:hu6 = _swig_property(_cv.CvHuMoments_hu6_get, _cv.CvHuMoments_hu6_set)
    __swig_setmethods__["hu7"] = _cv.CvHuMoments_hu7_set
    __swig_getmethods__["hu7"] = _cv.CvHuMoments_hu7_get
    if _newclass:hu7 = _swig_property(_cv.CvHuMoments_hu7_get, _cv.CvHuMoments_hu7_set)
    def __init__(self, *args): 
        """__init__(self) -> CvHuMoments"""
        this = _cv.new_CvHuMoments(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvHuMoments
    __del__ = lambda self : None;
CvHuMoments_swigregister = _cv.CvHuMoments_swigregister
CvHuMoments_swigregister(CvHuMoments)

class CvConnectedComp(_object):
    """Proxy of C++ CvConnectedComp class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvConnectedComp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvConnectedComp, name)
    __repr__ = _swig_repr
    __swig_setmethods__["area"] = _cv.CvConnectedComp_area_set
    __swig_getmethods__["area"] = _cv.CvConnectedComp_area_get
    if _newclass:area = _swig_property(_cv.CvConnectedComp_area_get, _cv.CvConnectedComp_area_set)
    __swig_setmethods__["value"] = _cv.CvConnectedComp_value_set
    __swig_getmethods__["value"] = _cv.CvConnectedComp_value_get
    if _newclass:value = _swig_property(_cv.CvConnectedComp_value_get, _cv.CvConnectedComp_value_set)
    __swig_setmethods__["rect"] = _cv.CvConnectedComp_rect_set
    __swig_getmethods__["rect"] = _cv.CvConnectedComp_rect_get
    if _newclass:rect = _swig_property(_cv.CvConnectedComp_rect_get, _cv.CvConnectedComp_rect_set)
    __swig_setmethods__["contour"] = _cv.CvConnectedComp_contour_set
    __swig_getmethods__["contour"] = _cv.CvConnectedComp_contour_get
    if _newclass:contour = _swig_property(_cv.CvConnectedComp_contour_get, _cv.CvConnectedComp_contour_set)
    def __init__(self, *args): 
        """__init__(self) -> CvConnectedComp"""
        this = _cv.new_CvConnectedComp(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvConnectedComp
    __del__ = lambda self : None;
CvConnectedComp_swigregister = _cv.CvConnectedComp_swigregister
CvConnectedComp_swigregister(CvConnectedComp)

class CvChainPtReader(_object):
    """Proxy of C++ CvChainPtReader class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvChainPtReader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvChainPtReader, name)
    __repr__ = _swig_repr
    __swig_setmethods__["header_size"] = _cv.CvChainPtReader_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvChainPtReader_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvChainPtReader_header_size_get, _cv.CvChainPtReader_header_size_set)
    __swig_setmethods__["seq"] = _cv.CvChainPtReader_seq_set
    __swig_getmethods__["seq"] = _cv.CvChainPtReader_seq_get
    if _newclass:seq = _swig_property(_cv.CvChainPtReader_seq_get, _cv.CvChainPtReader_seq_set)
    __swig_setmethods__["block"] = _cv.CvChainPtReader_block_set
    __swig_getmethods__["block"] = _cv.CvChainPtReader_block_get
    if _newclass:block = _swig_property(_cv.CvChainPtReader_block_get, _cv.CvChainPtReader_block_set)
    __swig_setmethods__["ptr"] = _cv.CvChainPtReader_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvChainPtReader_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvChainPtReader_ptr_get, _cv.CvChainPtReader_ptr_set)
    __swig_setmethods__["block_min"] = _cv.CvChainPtReader_block_min_set
    __swig_getmethods__["block_min"] = _cv.CvChainPtReader_block_min_get
    if _newclass:block_min = _swig_property(_cv.CvChainPtReader_block_min_get, _cv.CvChainPtReader_block_min_set)
    __swig_setmethods__["block_max"] = _cv.CvChainPtReader_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvChainPtReader_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvChainPtReader_block_max_get, _cv.CvChainPtReader_block_max_set)
    __swig_setmethods__["delta_index"] = _cv.CvChainPtReader_delta_index_set
    __swig_getmethods__["delta_index"] = _cv.CvChainPtReader_delta_index_get
    if _newclass:delta_index = _swig_property(_cv.CvChainPtReader_delta_index_get, _cv.CvChainPtReader_delta_index_set)
    __swig_setmethods__["prev_elem"] = _cv.CvChainPtReader_prev_elem_set
    __swig_getmethods__["prev_elem"] = _cv.CvChainPtReader_prev_elem_get
    if _newclass:prev_elem = _swig_property(_cv.CvChainPtReader_prev_elem_get, _cv.CvChainPtReader_prev_elem_set)
    __swig_setmethods__["code"] = _cv.CvChainPtReader_code_set
    __swig_getmethods__["code"] = _cv.CvChainPtReader_code_get
    if _newclass:code = _swig_property(_cv.CvChainPtReader_code_get, _cv.CvChainPtReader_code_set)
    __swig_setmethods__["pt"] = _cv.CvChainPtReader_pt_set
    __swig_getmethods__["pt"] = _cv.CvChainPtReader_pt_get
    if _newclass:pt = _swig_property(_cv.CvChainPtReader_pt_get, _cv.CvChainPtReader_pt_set)
    __swig_setmethods__["deltas"] = _cv.CvChainPtReader_deltas_set
    __swig_getmethods__["deltas"] = _cv.CvChainPtReader_deltas_get
    if _newclass:deltas = _swig_property(_cv.CvChainPtReader_deltas_get, _cv.CvChainPtReader_deltas_set)
    def __init__(self, *args): 
        """__init__(self) -> CvChainPtReader"""
        this = _cv.new_CvChainPtReader(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvChainPtReader
    __del__ = lambda self : None;
CvChainPtReader_swigregister = _cv.CvChainPtReader_swigregister
CvChainPtReader_swigregister(CvChainPtReader)

class CvContourTree(_object):
    """Proxy of C++ CvContourTree class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvContourTree, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvContourTree, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvContourTree_flags_set
    __swig_getmethods__["flags"] = _cv.CvContourTree_flags_get
    if _newclass:flags = _swig_property(_cv.CvContourTree_flags_get, _cv.CvContourTree_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvContourTree_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvContourTree_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvContourTree_header_size_get, _cv.CvContourTree_header_size_set)
    __swig_setmethods__["h_prev"] = _cv.CvContourTree_h_prev_set
    __swig_getmethods__["h_prev"] = _cv.CvContourTree_h_prev_get
    if _newclass:h_prev = _swig_property(_cv.CvContourTree_h_prev_get, _cv.CvContourTree_h_prev_set)
    __swig_setmethods__["h_next"] = _cv.CvContourTree_h_next_set
    __swig_getmethods__["h_next"] = _cv.CvContourTree_h_next_get
    if _newclass:h_next = _swig_property(_cv.CvContourTree_h_next_get, _cv.CvContourTree_h_next_set)
    __swig_setmethods__["v_prev"] = _cv.CvContourTree_v_prev_set
    __swig_getmethods__["v_prev"] = _cv.CvContourTree_v_prev_get
    if _newclass:v_prev = _swig_property(_cv.CvContourTree_v_prev_get, _cv.CvContourTree_v_prev_set)
    __swig_setmethods__["v_next"] = _cv.CvContourTree_v_next_set
    __swig_getmethods__["v_next"] = _cv.CvContourTree_v_next_get
    if _newclass:v_next = _swig_property(_cv.CvContourTree_v_next_get, _cv.CvContourTree_v_next_set)
    __swig_setmethods__["total"] = _cv.CvContourTree_total_set
    __swig_getmethods__["total"] = _cv.CvContourTree_total_get
    if _newclass:total = _swig_property(_cv.CvContourTree_total_get, _cv.CvContourTree_total_set)
    __swig_setmethods__["elem_size"] = _cv.CvContourTree_elem_size_set
    __swig_getmethods__["elem_size"] = _cv.CvContourTree_elem_size_get
    if _newclass:elem_size = _swig_property(_cv.CvContourTree_elem_size_get, _cv.CvContourTree_elem_size_set)
    __swig_setmethods__["block_max"] = _cv.CvContourTree_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvContourTree_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvContourTree_block_max_get, _cv.CvContourTree_block_max_set)
    __swig_setmethods__["ptr"] = _cv.CvContourTree_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvContourTree_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvContourTree_ptr_get, _cv.CvContourTree_ptr_set)
    __swig_setmethods__["delta_elems"] = _cv.CvContourTree_delta_elems_set
    __swig_getmethods__["delta_elems"] = _cv.CvContourTree_delta_elems_get
    if _newclass:delta_elems = _swig_property(_cv.CvContourTree_delta_elems_get, _cv.CvContourTree_delta_elems_set)
    __swig_setmethods__["storage"] = _cv.CvContourTree_storage_set
    __swig_getmethods__["storage"] = _cv.CvContourTree_storage_get
    if _newclass:storage = _swig_property(_cv.CvContourTree_storage_get, _cv.CvContourTree_storage_set)
    __swig_setmethods__["free_blocks"] = _cv.CvContourTree_free_blocks_set
    __swig_getmethods__["free_blocks"] = _cv.CvContourTree_free_blocks_get
    if _newclass:free_blocks = _swig_property(_cv.CvContourTree_free_blocks_get, _cv.CvContourTree_free_blocks_set)
    __swig_setmethods__["first"] = _cv.CvContourTree_first_set
    __swig_getmethods__["first"] = _cv.CvContourTree_first_get
    if _newclass:first = _swig_property(_cv.CvContourTree_first_get, _cv.CvContourTree_first_set)
    __swig_setmethods__["p1"] = _cv.CvContourTree_p1_set
    __swig_getmethods__["p1"] = _cv.CvContourTree_p1_get
    if _newclass:p1 = _swig_property(_cv.CvContourTree_p1_get, _cv.CvContourTree_p1_set)
    __swig_setmethods__["p2"] = _cv.CvContourTree_p2_set
    __swig_getmethods__["p2"] = _cv.CvContourTree_p2_get
    if _newclass:p2 = _swig_property(_cv.CvContourTree_p2_get, _cv.CvContourTree_p2_set)
    def __init__(self, *args): 
        """__init__(self) -> CvContourTree"""
        this = _cv.new_CvContourTree(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvContourTree
    __del__ = lambda self : None;
CvContourTree_swigregister = _cv.CvContourTree_swigregister
CvContourTree_swigregister(CvContourTree)

class CvConvexityDefect(_object):
    """Proxy of C++ CvConvexityDefect class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvConvexityDefect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvConvexityDefect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["start"] = _cv.CvConvexityDefect_start_set
    __swig_getmethods__["start"] = _cv.CvConvexityDefect_start_get
    if _newclass:start = _swig_property(_cv.CvConvexityDefect_start_get, _cv.CvConvexityDefect_start_set)
    __swig_setmethods__["end"] = _cv.CvConvexityDefect_end_set
    __swig_getmethods__["end"] = _cv.CvConvexityDefect_end_get
    if _newclass:end = _swig_property(_cv.CvConvexityDefect_end_get, _cv.CvConvexityDefect_end_set)
    __swig_setmethods__["depth_point"] = _cv.CvConvexityDefect_depth_point_set
    __swig_getmethods__["depth_point"] = _cv.CvConvexityDefect_depth_point_get
    if _newclass:depth_point = _swig_property(_cv.CvConvexityDefect_depth_point_get, _cv.CvConvexityDefect_depth_point_set)
    __swig_setmethods__["depth"] = _cv.CvConvexityDefect_depth_set
    __swig_getmethods__["depth"] = _cv.CvConvexityDefect_depth_get
    if _newclass:depth = _swig_property(_cv.CvConvexityDefect_depth_get, _cv.CvConvexityDefect_depth_set)
    def __init__(self, *args): 
        """__init__(self) -> CvConvexityDefect"""
        this = _cv.new_CvConvexityDefect(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvConvexityDefect
    __del__ = lambda self : None;
CvConvexityDefect_swigregister = _cv.CvConvexityDefect_swigregister
CvConvexityDefect_swigregister(CvConvexityDefect)

class CvQuadEdge2D(_object):
    """Proxy of C++ CvQuadEdge2D class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvQuadEdge2D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvQuadEdge2D, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvQuadEdge2D_flags_set
    __swig_getmethods__["flags"] = _cv.CvQuadEdge2D_flags_get
    if _newclass:flags = _swig_property(_cv.CvQuadEdge2D_flags_get, _cv.CvQuadEdge2D_flags_set)
    __swig_setmethods__["pt"] = _cv.CvQuadEdge2D_pt_set
    __swig_getmethods__["pt"] = _cv.CvQuadEdge2D_pt_get
    if _newclass:pt = _swig_property(_cv.CvQuadEdge2D_pt_get, _cv.CvQuadEdge2D_pt_set)
    __swig_setmethods__["next"] = _cv.CvQuadEdge2D_next_set
    __swig_getmethods__["next"] = _cv.CvQuadEdge2D_next_get
    if _newclass:next = _swig_property(_cv.CvQuadEdge2D_next_get, _cv.CvQuadEdge2D_next_set)
    def __init__(self, *args): 
        """__init__(self) -> CvQuadEdge2D"""
        this = _cv.new_CvQuadEdge2D(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvQuadEdge2D
    __del__ = lambda self : None;
CvQuadEdge2D_swigregister = _cv.CvQuadEdge2D_swigregister
CvQuadEdge2D_swigregister(CvQuadEdge2D)

class CvSubdiv2DPoint(_object):
    """Proxy of C++ CvSubdiv2DPoint class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSubdiv2DPoint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSubdiv2DPoint, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvSubdiv2DPoint_flags_set
    __swig_getmethods__["flags"] = _cv.CvSubdiv2DPoint_flags_get
    if _newclass:flags = _swig_property(_cv.CvSubdiv2DPoint_flags_get, _cv.CvSubdiv2DPoint_flags_set)
    __swig_setmethods__["first"] = _cv.CvSubdiv2DPoint_first_set
    __swig_getmethods__["first"] = _cv.CvSubdiv2DPoint_first_get
    if _newclass:first = _swig_property(_cv.CvSubdiv2DPoint_first_get, _cv.CvSubdiv2DPoint_first_set)
    __swig_setmethods__["pt"] = _cv.CvSubdiv2DPoint_pt_set
    __swig_getmethods__["pt"] = _cv.CvSubdiv2DPoint_pt_get
    if _newclass:pt = _swig_property(_cv.CvSubdiv2DPoint_pt_get, _cv.CvSubdiv2DPoint_pt_set)
    def __init__(self, *args): 
        """__init__(self) -> CvSubdiv2DPoint"""
        this = _cv.new_CvSubdiv2DPoint(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSubdiv2DPoint
    __del__ = lambda self : None;
CvSubdiv2DPoint_swigregister = _cv.CvSubdiv2DPoint_swigregister
CvSubdiv2DPoint_swigregister(CvSubdiv2DPoint)

class CvSubdiv2D(_object):
    """Proxy of C++ CvSubdiv2D class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSubdiv2D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvSubdiv2D, name)
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvSubdiv2D_flags_set
    __swig_getmethods__["flags"] = _cv.CvSubdiv2D_flags_get
    if _newclass:flags = _swig_property(_cv.CvSubdiv2D_flags_get, _cv.CvSubdiv2D_flags_set)
    __swig_setmethods__["header_size"] = _cv.CvSubdiv2D_header_size_set
    __swig_getmethods__["header_size"] = _cv.CvSubdiv2D_header_size_get
    if _newclass:header_size = _swig_property(_cv.CvSubdiv2D_header_size_get, _cv.CvSubdiv2D_header_size_set)
    __swig_setmethods__["h_prev"] = _cv.CvSubdiv2D_h_prev_set
    __swig_getmethods__["h_prev"] = _cv.CvSubdiv2D_h_prev_get
    if _newclass:h_prev = _swig_property(_cv.CvSubdiv2D_h_prev_get, _cv.CvSubdiv2D_h_prev_set)
    __swig_setmethods__["h_next"] = _cv.CvSubdiv2D_h_next_set
    __swig_getmethods__["h_next"] = _cv.CvSubdiv2D_h_next_get
    if _newclass:h_next = _swig_property(_cv.CvSubdiv2D_h_next_get, _cv.CvSubdiv2D_h_next_set)
    __swig_setmethods__["v_prev"] = _cv.CvSubdiv2D_v_prev_set
    __swig_getmethods__["v_prev"] = _cv.CvSubdiv2D_v_prev_get
    if _newclass:v_prev = _swig_property(_cv.CvSubdiv2D_v_prev_get, _cv.CvSubdiv2D_v_prev_set)
    __swig_setmethods__["v_next"] = _cv.CvSubdiv2D_v_next_set
    __swig_getmethods__["v_next"] = _cv.CvSubdiv2D_v_next_get
    if _newclass:v_next = _swig_property(_cv.CvSubdiv2D_v_next_get, _cv.CvSubdiv2D_v_next_set)
    __swig_setmethods__["total"] = _cv.CvSubdiv2D_total_set
    __swig_getmethods__["total"] = _cv.CvSubdiv2D_total_get
    if _newclass:total = _swig_property(_cv.CvSubdiv2D_total_get, _cv.CvSubdiv2D_total_set)
    __swig_setmethods__["elem_size"] = _cv.CvSubdiv2D_elem_size_set
    __swig_getmethods__["elem_size"] = _cv.CvSubdiv2D_elem_size_get
    if _newclass:elem_size = _swig_property(_cv.CvSubdiv2D_elem_size_get, _cv.CvSubdiv2D_elem_size_set)
    __swig_setmethods__["block_max"] = _cv.CvSubdiv2D_block_max_set
    __swig_getmethods__["block_max"] = _cv.CvSubdiv2D_block_max_get
    if _newclass:block_max = _swig_property(_cv.CvSubdiv2D_block_max_get, _cv.CvSubdiv2D_block_max_set)
    __swig_setmethods__["ptr"] = _cv.CvSubdiv2D_ptr_set
    __swig_getmethods__["ptr"] = _cv.CvSubdiv2D_ptr_get
    if _newclass:ptr = _swig_property(_cv.CvSubdiv2D_ptr_get, _cv.CvSubdiv2D_ptr_set)
    __swig_setmethods__["delta_elems"] = _cv.CvSubdiv2D_delta_elems_set
    __swig_getmethods__["delta_elems"] = _cv.CvSubdiv2D_delta_elems_get
    if _newclass:delta_elems = _swig_property(_cv.CvSubdiv2D_delta_elems_get, _cv.CvSubdiv2D_delta_elems_set)
    __swig_setmethods__["storage"] = _cv.CvSubdiv2D_storage_set
    __swig_getmethods__["storage"] = _cv.CvSubdiv2D_storage_get
    if _newclass:storage = _swig_property(_cv.CvSubdiv2D_storage_get, _cv.CvSubdiv2D_storage_set)
    __swig_setmethods__["free_blocks"] = _cv.CvSubdiv2D_free_blocks_set
    __swig_getmethods__["free_blocks"] = _cv.CvSubdiv2D_free_blocks_get
    if _newclass:free_blocks = _swig_property(_cv.CvSubdiv2D_free_blocks_get, _cv.CvSubdiv2D_free_blocks_set)
    __swig_setmethods__["first"] = _cv.CvSubdiv2D_first_set
    __swig_getmethods__["first"] = _cv.CvSubdiv2D_first_get
    if _newclass:first = _swig_property(_cv.CvSubdiv2D_first_get, _cv.CvSubdiv2D_first_set)
    __swig_setmethods__["free_elems"] = _cv.CvSubdiv2D_free_elems_set
    __swig_getmethods__["free_elems"] = _cv.CvSubdiv2D_free_elems_get
    if _newclass:free_elems = _swig_property(_cv.CvSubdiv2D_free_elems_get, _cv.CvSubdiv2D_free_elems_set)
    __swig_setmethods__["active_count"] = _cv.CvSubdiv2D_active_count_set
    __swig_getmethods__["active_count"] = _cv.CvSubdiv2D_active_count_get
    if _newclass:active_count = _swig_property(_cv.CvSubdiv2D_active_count_get, _cv.CvSubdiv2D_active_count_set)
    __swig_setmethods__["quad_edges"] = _cv.CvSubdiv2D_quad_edges_set
    __swig_getmethods__["quad_edges"] = _cv.CvSubdiv2D_quad_edges_get
    if _newclass:quad_edges = _swig_property(_cv.CvSubdiv2D_quad_edges_get, _cv.CvSubdiv2D_quad_edges_set)
    __swig_setmethods__["is_geometry_valid"] = _cv.CvSubdiv2D_is_geometry_valid_set
    __swig_getmethods__["is_geometry_valid"] = _cv.CvSubdiv2D_is_geometry_valid_get
    if _newclass:is_geometry_valid = _swig_property(_cv.CvSubdiv2D_is_geometry_valid_get, _cv.CvSubdiv2D_is_geometry_valid_set)
    __swig_setmethods__["recent_edge"] = _cv.CvSubdiv2D_recent_edge_set
    __swig_getmethods__["recent_edge"] = _cv.CvSubdiv2D_recent_edge_get
    if _newclass:recent_edge = _swig_property(_cv.CvSubdiv2D_recent_edge_get, _cv.CvSubdiv2D_recent_edge_set)
    __swig_setmethods__["topleft"] = _cv.CvSubdiv2D_topleft_set
    __swig_getmethods__["topleft"] = _cv.CvSubdiv2D_topleft_get
    if _newclass:topleft = _swig_property(_cv.CvSubdiv2D_topleft_get, _cv.CvSubdiv2D_topleft_set)
    __swig_setmethods__["bottomright"] = _cv.CvSubdiv2D_bottomright_set
    __swig_getmethods__["bottomright"] = _cv.CvSubdiv2D_bottomright_get
    if _newclass:bottomright = _swig_property(_cv.CvSubdiv2D_bottomright_get, _cv.CvSubdiv2D_bottomright_set)
    __swig_setmethods__["edges"] = _cv.CvSubdiv2D_edges_set
    __swig_getmethods__["edges"] = _cv.CvSubdiv2D_edges_get
    if _newclass:edges = _swig_property(_cv.CvSubdiv2D_edges_get, _cv.CvSubdiv2D_edges_set)
    def typed_edges_get(*args):
        """typed_edges_get(self) -> CvSeq_CvQuadEdge2D"""
        return _cv.CvSubdiv2D_typed_edges_get(*args)

    def typed_edges_set(*args):
        """typed_edges_set(self, CvSeq_CvQuadEdge2D ?)"""
        return _cv.CvSubdiv2D_typed_edges_set(*args)

    def __iter__(self):
    	s = CvSeq_QuadEdge2D.cast(self)
    	for i in range(s.total):
    		yield s[i]

    def __init__(self, *args): 
        """__init__(self) -> CvSubdiv2D"""
        this = _cv.new_CvSubdiv2D(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSubdiv2D
    __del__ = lambda self : None;
CvSubdiv2D_swigregister = _cv.CvSubdiv2D_swigregister
CvSubdiv2D_swigregister(CvSubdiv2D)

CV_PTLOC_ERROR = _cv.CV_PTLOC_ERROR
CV_PTLOC_OUTSIDE_RECT = _cv.CV_PTLOC_OUTSIDE_RECT
CV_PTLOC_INSIDE = _cv.CV_PTLOC_INSIDE
CV_PTLOC_VERTEX = _cv.CV_PTLOC_VERTEX
CV_PTLOC_ON_EDGE = _cv.CV_PTLOC_ON_EDGE
CV_NEXT_AROUND_ORG = _cv.CV_NEXT_AROUND_ORG
CV_NEXT_AROUND_DST = _cv.CV_NEXT_AROUND_DST
CV_PREV_AROUND_ORG = _cv.CV_PREV_AROUND_ORG
CV_PREV_AROUND_DST = _cv.CV_PREV_AROUND_DST
CV_NEXT_AROUND_LEFT = _cv.CV_NEXT_AROUND_LEFT
CV_NEXT_AROUND_RIGHT = _cv.CV_NEXT_AROUND_RIGHT
CV_PREV_AROUND_LEFT = _cv.CV_PREV_AROUND_LEFT
CV_PREV_AROUND_RIGHT = _cv.CV_PREV_AROUND_RIGHT
CV_GAUSSIAN_5x5 = _cv.CV_GAUSSIAN_5x5
class CvMatrix3(_object):
    """Proxy of C++ CvMatrix3 class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMatrix3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvMatrix3, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m"] = _cv.CvMatrix3_m_set
    __swig_getmethods__["m"] = _cv.CvMatrix3_m_get
    if _newclass:m = _swig_property(_cv.CvMatrix3_m_get, _cv.CvMatrix3_m_set)
    def __init__(self, *args): 
        """__init__(self) -> CvMatrix3"""
        this = _cv.new_CvMatrix3(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMatrix3
    __del__ = lambda self : None;
CvMatrix3_swigregister = _cv.CvMatrix3_swigregister
CvMatrix3_swigregister(CvMatrix3)

class CvConDensation(_object):
    """Proxy of C++ CvConDensation class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvConDensation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvConDensation, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["MP"] = _cv.CvConDensation_MP_set
    __swig_getmethods__["MP"] = _cv.CvConDensation_MP_get
    if _newclass:MP = _swig_property(_cv.CvConDensation_MP_get, _cv.CvConDensation_MP_set)
    __swig_setmethods__["DP"] = _cv.CvConDensation_DP_set
    __swig_getmethods__["DP"] = _cv.CvConDensation_DP_get
    if _newclass:DP = _swig_property(_cv.CvConDensation_DP_get, _cv.CvConDensation_DP_set)
    __swig_setmethods__["DynamMatr"] = _cv.CvConDensation_DynamMatr_set
    __swig_getmethods__["DynamMatr"] = _cv.CvConDensation_DynamMatr_get
    if _newclass:DynamMatr = _swig_property(_cv.CvConDensation_DynamMatr_get, _cv.CvConDensation_DynamMatr_set)
    __swig_setmethods__["State"] = _cv.CvConDensation_State_set
    __swig_getmethods__["State"] = _cv.CvConDensation_State_get
    if _newclass:State = _swig_property(_cv.CvConDensation_State_get, _cv.CvConDensation_State_set)
    __swig_setmethods__["SamplesNum"] = _cv.CvConDensation_SamplesNum_set
    __swig_getmethods__["SamplesNum"] = _cv.CvConDensation_SamplesNum_get
    if _newclass:SamplesNum = _swig_property(_cv.CvConDensation_SamplesNum_get, _cv.CvConDensation_SamplesNum_set)
    __swig_setmethods__["flSamples"] = _cv.CvConDensation_flSamples_set
    __swig_getmethods__["flSamples"] = _cv.CvConDensation_flSamples_get
    if _newclass:flSamples = _swig_property(_cv.CvConDensation_flSamples_get, _cv.CvConDensation_flSamples_set)
    __swig_setmethods__["flNewSamples"] = _cv.CvConDensation_flNewSamples_set
    __swig_getmethods__["flNewSamples"] = _cv.CvConDensation_flNewSamples_get
    if _newclass:flNewSamples = _swig_property(_cv.CvConDensation_flNewSamples_get, _cv.CvConDensation_flNewSamples_set)
    __swig_setmethods__["flConfidence"] = _cv.CvConDensation_flConfidence_set
    __swig_getmethods__["flConfidence"] = _cv.CvConDensation_flConfidence_get
    if _newclass:flConfidence = _swig_property(_cv.CvConDensation_flConfidence_get, _cv.CvConDensation_flConfidence_set)
    __swig_setmethods__["flCumulative"] = _cv.CvConDensation_flCumulative_set
    __swig_getmethods__["flCumulative"] = _cv.CvConDensation_flCumulative_get
    if _newclass:flCumulative = _swig_property(_cv.CvConDensation_flCumulative_get, _cv.CvConDensation_flCumulative_set)
    __swig_setmethods__["Temp"] = _cv.CvConDensation_Temp_set
    __swig_getmethods__["Temp"] = _cv.CvConDensation_Temp_get
    if _newclass:Temp = _swig_property(_cv.CvConDensation_Temp_get, _cv.CvConDensation_Temp_set)
    __swig_setmethods__["RandomSample"] = _cv.CvConDensation_RandomSample_set
    __swig_getmethods__["RandomSample"] = _cv.CvConDensation_RandomSample_get
    if _newclass:RandomSample = _swig_property(_cv.CvConDensation_RandomSample_get, _cv.CvConDensation_RandomSample_set)
    __swig_setmethods__["RandS"] = _cv.CvConDensation_RandS_set
    __swig_getmethods__["RandS"] = _cv.CvConDensation_RandS_get
    if _newclass:RandS = _swig_property(_cv.CvConDensation_RandS_get, _cv.CvConDensation_RandS_set)
    __swig_destroy__ = _cv.delete_CvConDensation
    __del__ = lambda self : None;
CvConDensation_swigregister = _cv.CvConDensation_swigregister
CvConDensation_swigregister(CvConDensation)

class CvKalman(_object):
    """Proxy of C++ CvKalman class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvKalman, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvKalman, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["MP"] = _cv.CvKalman_MP_set
    __swig_getmethods__["MP"] = _cv.CvKalman_MP_get
    if _newclass:MP = _swig_property(_cv.CvKalman_MP_get, _cv.CvKalman_MP_set)
    __swig_setmethods__["DP"] = _cv.CvKalman_DP_set
    __swig_getmethods__["DP"] = _cv.CvKalman_DP_get
    if _newclass:DP = _swig_property(_cv.CvKalman_DP_get, _cv.CvKalman_DP_set)
    __swig_setmethods__["CP"] = _cv.CvKalman_CP_set
    __swig_getmethods__["CP"] = _cv.CvKalman_CP_get
    if _newclass:CP = _swig_property(_cv.CvKalman_CP_get, _cv.CvKalman_CP_set)
    __swig_setmethods__["PosterState"] = _cv.CvKalman_PosterState_set
    __swig_getmethods__["PosterState"] = _cv.CvKalman_PosterState_get
    if _newclass:PosterState = _swig_property(_cv.CvKalman_PosterState_get, _cv.CvKalman_PosterState_set)
    __swig_setmethods__["PriorState"] = _cv.CvKalman_PriorState_set
    __swig_getmethods__["PriorState"] = _cv.CvKalman_PriorState_get
    if _newclass:PriorState = _swig_property(_cv.CvKalman_PriorState_get, _cv.CvKalman_PriorState_set)
    __swig_setmethods__["DynamMatr"] = _cv.CvKalman_DynamMatr_set
    __swig_getmethods__["DynamMatr"] = _cv.CvKalman_DynamMatr_get
    if _newclass:DynamMatr = _swig_property(_cv.CvKalman_DynamMatr_get, _cv.CvKalman_DynamMatr_set)
    __swig_setmethods__["MeasurementMatr"] = _cv.CvKalman_MeasurementMatr_set
    __swig_getmethods__["MeasurementMatr"] = _cv.CvKalman_MeasurementMatr_get
    if _newclass:MeasurementMatr = _swig_property(_cv.CvKalman_MeasurementMatr_get, _cv.CvKalman_MeasurementMatr_set)
    __swig_setmethods__["MNCovariance"] = _cv.CvKalman_MNCovariance_set
    __swig_getmethods__["MNCovariance"] = _cv.CvKalman_MNCovariance_get
    if _newclass:MNCovariance = _swig_property(_cv.CvKalman_MNCovariance_get, _cv.CvKalman_MNCovariance_set)
    __swig_setmethods__["PNCovariance"] = _cv.CvKalman_PNCovariance_set
    __swig_getmethods__["PNCovariance"] = _cv.CvKalman_PNCovariance_get
    if _newclass:PNCovariance = _swig_property(_cv.CvKalman_PNCovariance_get, _cv.CvKalman_PNCovariance_set)
    __swig_setmethods__["KalmGainMatr"] = _cv.CvKalman_KalmGainMatr_set
    __swig_getmethods__["KalmGainMatr"] = _cv.CvKalman_KalmGainMatr_get
    if _newclass:KalmGainMatr = _swig_property(_cv.CvKalman_KalmGainMatr_get, _cv.CvKalman_KalmGainMatr_set)
    __swig_setmethods__["PriorErrorCovariance"] = _cv.CvKalman_PriorErrorCovariance_set
    __swig_getmethods__["PriorErrorCovariance"] = _cv.CvKalman_PriorErrorCovariance_get
    if _newclass:PriorErrorCovariance = _swig_property(_cv.CvKalman_PriorErrorCovariance_get, _cv.CvKalman_PriorErrorCovariance_set)
    __swig_setmethods__["PosterErrorCovariance"] = _cv.CvKalman_PosterErrorCovariance_set
    __swig_getmethods__["PosterErrorCovariance"] = _cv.CvKalman_PosterErrorCovariance_get
    if _newclass:PosterErrorCovariance = _swig_property(_cv.CvKalman_PosterErrorCovariance_get, _cv.CvKalman_PosterErrorCovariance_set)
    __swig_setmethods__["Temp1"] = _cv.CvKalman_Temp1_set
    __swig_getmethods__["Temp1"] = _cv.CvKalman_Temp1_get
    if _newclass:Temp1 = _swig_property(_cv.CvKalman_Temp1_get, _cv.CvKalman_Temp1_set)
    __swig_setmethods__["Temp2"] = _cv.CvKalman_Temp2_set
    __swig_getmethods__["Temp2"] = _cv.CvKalman_Temp2_get
    if _newclass:Temp2 = _swig_property(_cv.CvKalman_Temp2_get, _cv.CvKalman_Temp2_set)
    __swig_setmethods__["state_pre"] = _cv.CvKalman_state_pre_set
    __swig_getmethods__["state_pre"] = _cv.CvKalman_state_pre_get
    if _newclass:state_pre = _swig_property(_cv.CvKalman_state_pre_get, _cv.CvKalman_state_pre_set)
    __swig_setmethods__["state_post"] = _cv.CvKalman_state_post_set
    __swig_getmethods__["state_post"] = _cv.CvKalman_state_post_get
    if _newclass:state_post = _swig_property(_cv.CvKalman_state_post_get, _cv.CvKalman_state_post_set)
    __swig_setmethods__["transition_matrix"] = _cv.CvKalman_transition_matrix_set
    __swig_getmethods__["transition_matrix"] = _cv.CvKalman_transition_matrix_get
    if _newclass:transition_matrix = _swig_property(_cv.CvKalman_transition_matrix_get, _cv.CvKalman_transition_matrix_set)
    __swig_setmethods__["control_matrix"] = _cv.CvKalman_control_matrix_set
    __swig_getmethods__["control_matrix"] = _cv.CvKalman_control_matrix_get
    if _newclass:control_matrix = _swig_property(_cv.CvKalman_control_matrix_get, _cv.CvKalman_control_matrix_set)
    __swig_setmethods__["measurement_matrix"] = _cv.CvKalman_measurement_matrix_set
    __swig_getmethods__["measurement_matrix"] = _cv.CvKalman_measurement_matrix_get
    if _newclass:measurement_matrix = _swig_property(_cv.CvKalman_measurement_matrix_get, _cv.CvKalman_measurement_matrix_set)
    __swig_setmethods__["process_noise_cov"] = _cv.CvKalman_process_noise_cov_set
    __swig_getmethods__["process_noise_cov"] = _cv.CvKalman_process_noise_cov_get
    if _newclass:process_noise_cov = _swig_property(_cv.CvKalman_process_noise_cov_get, _cv.CvKalman_process_noise_cov_set)
    __swig_setmethods__["measurement_noise_cov"] = _cv.CvKalman_measurement_noise_cov_set
    __swig_getmethods__["measurement_noise_cov"] = _cv.CvKalman_measurement_noise_cov_get
    if _newclass:measurement_noise_cov = _swig_property(_cv.CvKalman_measurement_noise_cov_get, _cv.CvKalman_measurement_noise_cov_set)
    __swig_setmethods__["error_cov_pre"] = _cv.CvKalman_error_cov_pre_set
    __swig_getmethods__["error_cov_pre"] = _cv.CvKalman_error_cov_pre_get
    if _newclass:error_cov_pre = _swig_property(_cv.CvKalman_error_cov_pre_get, _cv.CvKalman_error_cov_pre_set)
    __swig_setmethods__["gain"] = _cv.CvKalman_gain_set
    __swig_getmethods__["gain"] = _cv.CvKalman_gain_get
    if _newclass:gain = _swig_property(_cv.CvKalman_gain_get, _cv.CvKalman_gain_set)
    __swig_setmethods__["error_cov_post"] = _cv.CvKalman_error_cov_post_set
    __swig_getmethods__["error_cov_post"] = _cv.CvKalman_error_cov_post_get
    if _newclass:error_cov_post = _swig_property(_cv.CvKalman_error_cov_post_get, _cv.CvKalman_error_cov_post_set)
    __swig_setmethods__["temp1"] = _cv.CvKalman_temp1_set
    __swig_getmethods__["temp1"] = _cv.CvKalman_temp1_get
    if _newclass:temp1 = _swig_property(_cv.CvKalman_temp1_get, _cv.CvKalman_temp1_set)
    __swig_setmethods__["temp2"] = _cv.CvKalman_temp2_set
    __swig_getmethods__["temp2"] = _cv.CvKalman_temp2_get
    if _newclass:temp2 = _swig_property(_cv.CvKalman_temp2_get, _cv.CvKalman_temp2_set)
    __swig_setmethods__["temp3"] = _cv.CvKalman_temp3_set
    __swig_getmethods__["temp3"] = _cv.CvKalman_temp3_get
    if _newclass:temp3 = _swig_property(_cv.CvKalman_temp3_get, _cv.CvKalman_temp3_set)
    __swig_setmethods__["temp4"] = _cv.CvKalman_temp4_set
    __swig_getmethods__["temp4"] = _cv.CvKalman_temp4_get
    if _newclass:temp4 = _swig_property(_cv.CvKalman_temp4_get, _cv.CvKalman_temp4_set)
    __swig_setmethods__["temp5"] = _cv.CvKalman_temp5_set
    __swig_getmethods__["temp5"] = _cv.CvKalman_temp5_get
    if _newclass:temp5 = _swig_property(_cv.CvKalman_temp5_get, _cv.CvKalman_temp5_set)
    __swig_destroy__ = _cv.delete_CvKalman
    __del__ = lambda self : None;
CvKalman_swigregister = _cv.CvKalman_swigregister
CvKalman_swigregister(CvKalman)

class CvHaarFeature(_object):
    """Proxy of C++ CvHaarFeature class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvHaarFeature, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvHaarFeature, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tilted"] = _cv.CvHaarFeature_tilted_set
    __swig_getmethods__["tilted"] = _cv.CvHaarFeature_tilted_get
    if _newclass:tilted = _swig_property(_cv.CvHaarFeature_tilted_get, _cv.CvHaarFeature_tilted_set)
    __swig_getmethods__["rect"] = _cv.CvHaarFeature_rect_get
    if _newclass:rect = _swig_property(_cv.CvHaarFeature_rect_get)
    def __init__(self, *args): 
        """__init__(self) -> CvHaarFeature"""
        this = _cv.new_CvHaarFeature(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvHaarFeature
    __del__ = lambda self : None;
CvHaarFeature_swigregister = _cv.CvHaarFeature_swigregister
CvHaarFeature_swigregister(CvHaarFeature)

class CvHaarFeature_rect(_object):
    """Proxy of C++ CvHaarFeature_rect class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvHaarFeature_rect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvHaarFeature_rect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["r"] = _cv.CvHaarFeature_rect_r_set
    __swig_getmethods__["r"] = _cv.CvHaarFeature_rect_r_get
    if _newclass:r = _swig_property(_cv.CvHaarFeature_rect_r_get, _cv.CvHaarFeature_rect_r_set)
    __swig_setmethods__["weight"] = _cv.CvHaarFeature_rect_weight_set
    __swig_getmethods__["weight"] = _cv.CvHaarFeature_rect_weight_get
    if _newclass:weight = _swig_property(_cv.CvHaarFeature_rect_weight_get, _cv.CvHaarFeature_rect_weight_set)
    def __init__(self, *args): 
        """__init__(self) -> CvHaarFeature_rect"""
        this = _cv.new_CvHaarFeature_rect(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvHaarFeature_rect
    __del__ = lambda self : None;
CvHaarFeature_rect_swigregister = _cv.CvHaarFeature_rect_swigregister
CvHaarFeature_rect_swigregister(CvHaarFeature_rect)

class CvHaarClassifier(_object):
    """Proxy of C++ CvHaarClassifier class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvHaarClassifier, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvHaarClassifier, name)
    __repr__ = _swig_repr
    __swig_setmethods__["count"] = _cv.CvHaarClassifier_count_set
    __swig_getmethods__["count"] = _cv.CvHaarClassifier_count_get
    if _newclass:count = _swig_property(_cv.CvHaarClassifier_count_get, _cv.CvHaarClassifier_count_set)
    __swig_setmethods__["haar_feature"] = _cv.CvHaarClassifier_haar_feature_set
    __swig_getmethods__["haar_feature"] = _cv.CvHaarClassifier_haar_feature_get
    if _newclass:haar_feature = _swig_property(_cv.CvHaarClassifier_haar_feature_get, _cv.CvHaarClassifier_haar_feature_set)
    __swig_setmethods__["threshold"] = _cv.CvHaarClassifier_threshold_set
    __swig_getmethods__["threshold"] = _cv.CvHaarClassifier_threshold_get
    if _newclass:threshold = _swig_property(_cv.CvHaarClassifier_threshold_get, _cv.CvHaarClassifier_threshold_set)
    __swig_setmethods__["left"] = _cv.CvHaarClassifier_left_set
    __swig_getmethods__["left"] = _cv.CvHaarClassifier_left_get
    if _newclass:left = _swig_property(_cv.CvHaarClassifier_left_get, _cv.CvHaarClassifier_left_set)
    __swig_setmethods__["right"] = _cv.CvHaarClassifier_right_set
    __swig_getmethods__["right"] = _cv.CvHaarClassifier_right_get
    if _newclass:right = _swig_property(_cv.CvHaarClassifier_right_get, _cv.CvHaarClassifier_right_set)
    __swig_setmethods__["alpha"] = _cv.CvHaarClassifier_alpha_set
    __swig_getmethods__["alpha"] = _cv.CvHaarClassifier_alpha_get
    if _newclass:alpha = _swig_property(_cv.CvHaarClassifier_alpha_get, _cv.CvHaarClassifier_alpha_set)
    def __init__(self, *args): 
        """__init__(self) -> CvHaarClassifier"""
        this = _cv.new_CvHaarClassifier(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvHaarClassifier
    __del__ = lambda self : None;
CvHaarClassifier_swigregister = _cv.CvHaarClassifier_swigregister
CvHaarClassifier_swigregister(CvHaarClassifier)

class CvHaarStageClassifier(_object):
    """Proxy of C++ CvHaarStageClassifier class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvHaarStageClassifier, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvHaarStageClassifier, name)
    __repr__ = _swig_repr
    __swig_setmethods__["count"] = _cv.CvHaarStageClassifier_count_set
    __swig_getmethods__["count"] = _cv.CvHaarStageClassifier_count_get
    if _newclass:count = _swig_property(_cv.CvHaarStageClassifier_count_get, _cv.CvHaarStageClassifier_count_set)
    __swig_setmethods__["threshold"] = _cv.CvHaarStageClassifier_threshold_set
    __swig_getmethods__["threshold"] = _cv.CvHaarStageClassifier_threshold_get
    if _newclass:threshold = _swig_property(_cv.CvHaarStageClassifier_threshold_get, _cv.CvHaarStageClassifier_threshold_set)
    __swig_setmethods__["classifier"] = _cv.CvHaarStageClassifier_classifier_set
    __swig_getmethods__["classifier"] = _cv.CvHaarStageClassifier_classifier_get
    if _newclass:classifier = _swig_property(_cv.CvHaarStageClassifier_classifier_get, _cv.CvHaarStageClassifier_classifier_set)
    __swig_setmethods__["next"] = _cv.CvHaarStageClassifier_next_set
    __swig_getmethods__["next"] = _cv.CvHaarStageClassifier_next_get
    if _newclass:next = _swig_property(_cv.CvHaarStageClassifier_next_get, _cv.CvHaarStageClassifier_next_set)
    __swig_setmethods__["child"] = _cv.CvHaarStageClassifier_child_set
    __swig_getmethods__["child"] = _cv.CvHaarStageClassifier_child_get
    if _newclass:child = _swig_property(_cv.CvHaarStageClassifier_child_get, _cv.CvHaarStageClassifier_child_set)
    __swig_setmethods__["parent"] = _cv.CvHaarStageClassifier_parent_set
    __swig_getmethods__["parent"] = _cv.CvHaarStageClassifier_parent_get
    if _newclass:parent = _swig_property(_cv.CvHaarStageClassifier_parent_get, _cv.CvHaarStageClassifier_parent_set)
    def __init__(self, *args): 
        """__init__(self) -> CvHaarStageClassifier"""
        this = _cv.new_CvHaarStageClassifier(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvHaarStageClassifier
    __del__ = lambda self : None;
CvHaarStageClassifier_swigregister = _cv.CvHaarStageClassifier_swigregister
CvHaarStageClassifier_swigregister(CvHaarStageClassifier)

class CvHaarClassifierCascade(_object):
    """Proxy of C++ CvHaarClassifierCascade class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvHaarClassifierCascade, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvHaarClassifierCascade, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_setmethods__["flags"] = _cv.CvHaarClassifierCascade_flags_set
    __swig_getmethods__["flags"] = _cv.CvHaarClassifierCascade_flags_get
    if _newclass:flags = _swig_property(_cv.CvHaarClassifierCascade_flags_get, _cv.CvHaarClassifierCascade_flags_set)
    __swig_setmethods__["count"] = _cv.CvHaarClassifierCascade_count_set
    __swig_getmethods__["count"] = _cv.CvHaarClassifierCascade_count_get
    if _newclass:count = _swig_property(_cv.CvHaarClassifierCascade_count_get, _cv.CvHaarClassifierCascade_count_set)
    __swig_setmethods__["orig_window_size"] = _cv.CvHaarClassifierCascade_orig_window_size_set
    __swig_getmethods__["orig_window_size"] = _cv.CvHaarClassifierCascade_orig_window_size_get
    if _newclass:orig_window_size = _swig_property(_cv.CvHaarClassifierCascade_orig_window_size_get, _cv.CvHaarClassifierCascade_orig_window_size_set)
    __swig_setmethods__["real_window_size"] = _cv.CvHaarClassifierCascade_real_window_size_set
    __swig_getmethods__["real_window_size"] = _cv.CvHaarClassifierCascade_real_window_size_get
    if _newclass:real_window_size = _swig_property(_cv.CvHaarClassifierCascade_real_window_size_get, _cv.CvHaarClassifierCascade_real_window_size_set)
    __swig_setmethods__["scale"] = _cv.CvHaarClassifierCascade_scale_set
    __swig_getmethods__["scale"] = _cv.CvHaarClassifierCascade_scale_get
    if _newclass:scale = _swig_property(_cv.CvHaarClassifierCascade_scale_get, _cv.CvHaarClassifierCascade_scale_set)
    __swig_setmethods__["stage_classifier"] = _cv.CvHaarClassifierCascade_stage_classifier_set
    __swig_getmethods__["stage_classifier"] = _cv.CvHaarClassifierCascade_stage_classifier_get
    if _newclass:stage_classifier = _swig_property(_cv.CvHaarClassifierCascade_stage_classifier_get, _cv.CvHaarClassifierCascade_stage_classifier_set)
    __swig_setmethods__["hid_cascade"] = _cv.CvHaarClassifierCascade_hid_cascade_set
    __swig_getmethods__["hid_cascade"] = _cv.CvHaarClassifierCascade_hid_cascade_get
    if _newclass:hid_cascade = _swig_property(_cv.CvHaarClassifierCascade_hid_cascade_get, _cv.CvHaarClassifierCascade_hid_cascade_set)
    __swig_destroy__ = _cv.delete_CvHaarClassifierCascade
    __del__ = lambda self : None;
CvHaarClassifierCascade_swigregister = _cv.CvHaarClassifierCascade_swigregister
CvHaarClassifierCascade_swigregister(CvHaarClassifierCascade)

class CvAvgComp(_object):
    """Proxy of C++ CvAvgComp class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvAvgComp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvAvgComp, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rect"] = _cv.CvAvgComp_rect_set
    __swig_getmethods__["rect"] = _cv.CvAvgComp_rect_get
    if _newclass:rect = _swig_property(_cv.CvAvgComp_rect_get, _cv.CvAvgComp_rect_set)
    __swig_setmethods__["neighbors"] = _cv.CvAvgComp_neighbors_set
    __swig_getmethods__["neighbors"] = _cv.CvAvgComp_neighbors_get
    if _newclass:neighbors = _swig_property(_cv.CvAvgComp_neighbors_get, _cv.CvAvgComp_neighbors_set)
    def __init__(self, *args): 
        """__init__(self) -> CvAvgComp"""
        this = _cv.new_CvAvgComp(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvAvgComp
    __del__ = lambda self : None;
CvAvgComp_swigregister = _cv.CvAvgComp_swigregister
CvAvgComp_swigregister(CvAvgComp)


def cvCopyMakeBorder(*args):
  """
    cvCopyMakeBorder(CvArr src, CvArr dst, CvPoint offset, int bordertype, 
        CvScalar value=cvScalarAll(0))
    """
  return _cv.cvCopyMakeBorder(*args)

def cvSmooth(*args):
  """
    cvSmooth(CvArr src, CvArr dst, int smoothtype=2, int param1=3, 
        int param2=0, double param3=0, double param4=0)
    """
  return _cv.cvSmooth(*args)

def cvFilter2D(*args):
  """cvFilter2D(CvArr src, CvArr dst, CvMat kernel, CvPoint anchor=cvPoint(-1,-1))"""
  return _cv.cvFilter2D(*args)

def cvIntegral(*args):
  """cvIntegral(CvArr image, CvArr sum, CvArr sqsum=None, CvArr tilted_sum=None)"""
  return _cv.cvIntegral(*args)

def cvPyrDown(*args):
  """cvPyrDown(CvArr src, CvArr dst, int filter=CV_GAUSSIAN_5x5)"""
  return _cv.cvPyrDown(*args)

def cvPyrUp(*args):
  """cvPyrUp(CvArr src, CvArr dst, int filter=CV_GAUSSIAN_5x5)"""
  return _cv.cvPyrUp(*args)

def cvPyrSegmentationUntyped(*args):
  """
    cvPyrSegmentationUntyped( src,  dst, CvMemStorage storage, CvSeq comp, int level, 
        double threshold1, double threshold2)
    """
  return _cv.cvPyrSegmentationUntyped(*args)

def cvPyrMeanShiftFiltering(*args):
  """
    cvPyrMeanShiftFiltering(CvArr src, CvArr dst, double sp, double sr, int max_level=1, 
        CvTermCriteria termcrit=cvTermCriteria(1 +2,5,1))
    """
  return _cv.cvPyrMeanShiftFiltering(*args)

def cvWatershed(*args):
  """cvWatershed(CvArr image, CvArr markers)"""
  return _cv.cvWatershed(*args)

def cvInpaint(*args):
  """
    cvInpaint(CvArr src, CvArr inpaint_mask, CvArr dst, double inpaintRange, 
        int flags)
    """
  return _cv.cvInpaint(*args)

def cvSobel(*args):
  """cvSobel(CvArr src, CvArr dst, int xorder, int yorder, int aperture_size=3)"""
  return _cv.cvSobel(*args)

def cvLaplace(*args):
  """cvLaplace(CvArr src, CvArr dst, int aperture_size=3)"""
  return _cv.cvLaplace(*args)

def cvCvtColor(*args):
  """cvCvtColor(CvArr src, CvArr dst, int code)"""
  return _cv.cvCvtColor(*args)

def cvResize(*args):
  """cvResize(CvArr src, CvArr dst, int interpolation=1)"""
  return _cv.cvResize(*args)

def cvWarpAffine(*args):
  """
    cvWarpAffine(CvArr src, CvArr dst, CvMat map_matrix, int flags=1+8, 
        CvScalar fillval=cvScalarAll(0))
    """
  return _cv.cvWarpAffine(*args)

def cvGetAffineTransform(*args):
  """cvGetAffineTransform(CvPoint2D32f src, CvPoint2D32f dst, CvMat map_matrix) -> CvMat"""
  return _cv.cvGetAffineTransform(*args)

def cv2DRotationMatrix(*args):
  """cv2DRotationMatrix(CvPoint2D32f center, double angle, double scale, CvMat map_matrix) -> CvMat"""
  return _cv.cv2DRotationMatrix(*args)

def cvWarpPerspective(*args):
  """
    cvWarpPerspective(CvArr src, CvArr dst, CvMat map_matrix, int flags=1+8, 
        CvScalar fillval=cvScalarAll(0))
    """
  return _cv.cvWarpPerspective(*args)

def cvGetPerspectiveTransform(*args):
  """cvGetPerspectiveTransform(CvPoint2D32f src, CvPoint2D32f dst, CvMat map_matrix) -> CvMat"""
  return _cv.cvGetPerspectiveTransform(*args)

def cvRemap(*args):
  """
    cvRemap(CvArr src, CvArr dst, CvArr mapx, CvArr mapy, int flags=1+8, 
        CvScalar fillval=cvScalarAll(0))
    """
  return _cv.cvRemap(*args)

def cvLogPolar(*args):
  """
    cvLogPolar(CvArr src, CvArr dst, CvPoint2D32f center, double M, 
        int flags=1+8)
    """
  return _cv.cvLogPolar(*args)

def cvCreateStructuringElementEx(*args):
  """
    cvCreateStructuringElementEx(int cols, int rows, int anchor_x, int anchor_y, int shape, 
        int values=None)
    """
  return _cv.cvCreateStructuringElementEx(*args)

def cvErode(*args):
  """cvErode(CvArr src, CvArr dst,  element=None, int iterations=1)"""
  return _cv.cvErode(*args)

def cvDilate(*args):
  """cvDilate(CvArr src, CvArr dst,  element=None, int iterations=1)"""
  return _cv.cvDilate(*args)

def cvMorphologyEx(*args):
  """
    cvMorphologyEx(CvArr src, CvArr dst, CvArr temp,  element, int operation, 
        int iterations=1)
    """
  return _cv.cvMorphologyEx(*args)

def cvMoments(*args):
  """cvMoments(CvArr arr, CvMoments moments, int binary=0)"""
  return _cv.cvMoments(*args)

def cvGetSpatialMoment(*args):
  """cvGetSpatialMoment(CvMoments moments, int x_order, int y_order) -> double"""
  return _cv.cvGetSpatialMoment(*args)

def cvGetCentralMoment(*args):
  """cvGetCentralMoment(CvMoments moments, int x_order, int y_order) -> double"""
  return _cv.cvGetCentralMoment(*args)

def cvGetNormalizedCentralMoment(*args):
  """cvGetNormalizedCentralMoment(CvMoments moments, int x_order, int y_order) -> double"""
  return _cv.cvGetNormalizedCentralMoment(*args)

def cvGetHuMoments(*args):
  """cvGetHuMoments(CvMoments moments, CvHuMoments hu_moments)"""
  return _cv.cvGetHuMoments(*args)

def cvSampleLine(*args):
  """
    cvSampleLine(CvArr image, CvPoint pt1, CvPoint pt2, void buffer, 
        int connectivity=8) -> int
    """
  return _cv.cvSampleLine(*args)

def cvGetRectSubPix(*args):
  """cvGetRectSubPix(CvArr src, CvArr dst, CvPoint2D32f center)"""
  return _cv.cvGetRectSubPix(*args)

def cvGetQuadrangleSubPix(*args):
  """cvGetQuadrangleSubPix(CvArr src, CvArr dst, CvMat map_matrix)"""
  return _cv.cvGetQuadrangleSubPix(*args)

def cvMatchTemplate(*args):
  """cvMatchTemplate(CvArr image, CvArr templ, CvArr result, int method)"""
  return _cv.cvMatchTemplate(*args)

def cvCalcEMD2(*args):
  """
    cvCalcEMD2(CvArr signature1, CvArr signature2, int distance_type, 
        CvDistanceFunction distance_func=None, CvArr cost_matrix=None, 
        CvArr flow=None, float lower_bound=None, 
        void userdata=None) -> float
    """
  return _cv.cvCalcEMD2(*args)

def cvFindContoursUntyped(*args):
  """
    cvFindContoursUntyped(CvArr image, CvMemStorage storage, CvSeq first_contour, 
        int header_size=sizeof(CvContour), int mode=1, 
        int method=2, CvPoint offset=cvPoint(0,0)) -> int
    """
  return _cv.cvFindContoursUntyped(*args)

def cvStartFindContours(*args):
  """
    cvStartFindContours(CvArr image, CvMemStorage storage, int header_size=sizeof(CvContour), 
        int mode=1, int method=2, 
        CvPoint offset=cvPoint(0,0)) -> CvContourScanner
    """
  return _cv.cvStartFindContours(*args)

def cvFindNextContour(*args):
  """cvFindNextContour(CvContourScanner scanner) -> CvSeq"""
  return _cv.cvFindNextContour(*args)

def cvSubstituteContour(*args):
  """cvSubstituteContour(CvContourScanner scanner, CvSeq new_contour)"""
  return _cv.cvSubstituteContour(*args)

def cvEndFindContours(*args):
  """cvEndFindContours(CvContourScanner scanner) -> CvSeq"""
  return _cv.cvEndFindContours(*args)

def cvApproxChainsUntyped(*args):
  """
    cvApproxChainsUntyped(CvSeq src_seq, CvMemStorage storage, int method=2, 
        double parameter=0, int minimal_perimeter=0, 
        int recursive=0) -> CvSeq
    """
  return _cv.cvApproxChainsUntyped(*args)

def cvStartReadChainPoints(*args):
  """cvStartReadChainPoints(CvChain chain, CvChainPtReader reader)"""
  return _cv.cvStartReadChainPoints(*args)

def cvReadChainPoint(*args):
  """cvReadChainPoint(CvChainPtReader reader) -> CvPoint"""
  return _cv.cvReadChainPoint(*args)

def cvCalcOpticalFlowLK(*args):
  """
    cvCalcOpticalFlowLK(CvArr prev, CvArr curr, CvSize win_size, CvArr velx, 
        CvArr vely)
    """
  return _cv.cvCalcOpticalFlowLK(*args)

def cvCalcOpticalFlowBM(*args):
  """
    cvCalcOpticalFlowBM(CvArr prev, CvArr curr, CvSize block_size, CvSize shift_size, 
        CvSize max_range, int use_previous, 
        CvArr velx, CvArr vely)
    """
  return _cv.cvCalcOpticalFlowBM(*args)

def cvCalcOpticalFlowHS(*args):
  """
    cvCalcOpticalFlowHS(CvArr prev, CvArr curr, int use_previous, CvArr velx, 
        CvArr vely, double lambda, CvTermCriteria criteria)
    """
  return _cv.cvCalcOpticalFlowHS(*args)

def cvCalcOpticalFlowPyrLK(*args):
  """
    cvCalcOpticalFlowPyrLK(CvArr prev, CvArr curr, CvArr prev_pyr, CvArr curr_pyr, 
        CvPoint2D32f prev_features, CvPoint2D32f curr_features, 
        CvSize win_size, int level, char status, 
        float track_error, CvTermCriteria criteria, 
        int flags)
    """
  return _cv.cvCalcOpticalFlowPyrLK(*args)

def cvUpdateMotionHistory(*args):
  """cvUpdateMotionHistory(CvArr silhouette, CvArr mhi, double timestamp, double duration)"""
  return _cv.cvUpdateMotionHistory(*args)

def cvCalcMotionGradient(*args):
  """
    cvCalcMotionGradient(CvArr mhi, CvArr mask, CvArr orientation, double delta1, 
        double delta2, int aperture_size=3)
    """
  return _cv.cvCalcMotionGradient(*args)

def cvCalcGlobalOrientation(*args):
  """
    cvCalcGlobalOrientation(CvArr orientation, CvArr mask, CvArr mhi, double timestamp, 
        double duration) -> double
    """
  return _cv.cvCalcGlobalOrientation(*args)

def cvAcc(*args):
  """cvAcc(CvArr image, CvArr sum, CvArr mask=None)"""
  return _cv.cvAcc(*args)

def cvSquareAcc(*args):
  """cvSquareAcc(CvArr image, CvArr sqsum, CvArr mask=None)"""
  return _cv.cvSquareAcc(*args)

def cvMultiplyAcc(*args):
  """cvMultiplyAcc(CvArr image1, CvArr image2, CvArr acc, CvArr mask=None)"""
  return _cv.cvMultiplyAcc(*args)

def cvRunningAvg(*args):
  """cvRunningAvg(CvArr image, CvArr acc, double alpha, CvArr mask=None)"""
  return _cv.cvRunningAvg(*args)

def cvCamShift(*args):
  """
    cvCamShift(CvArr prob_image, CvRect window, CvTermCriteria criteria, 
        CvConnectedComp comp, CvBox2D box=None) -> int
    """
  return _cv.cvCamShift(*args)

def cvMeanShift(*args):
  """
    cvMeanShift(CvArr prob_image, CvRect window, CvTermCriteria criteria, 
        CvConnectedComp comp) -> int
    """
  return _cv.cvMeanShift(*args)

def cvCreateConDensation(*args):
  """cvCreateConDensation(int dynam_params, int measure_params, int sample_count) -> CvConDensation"""
  return _cv.cvCreateConDensation(*args)

def cvConDensUpdateByTime(*args):
  """cvConDensUpdateByTime(CvConDensation condens)"""
  return _cv.cvConDensUpdateByTime(*args)

def cvConDensInitSampleSet(*args):
  """cvConDensInitSampleSet(CvConDensation condens, CvMat lower_bound, CvMat upper_bound)"""
  return _cv.cvConDensInitSampleSet(*args)

def cvCreateKalman(*args):
  """cvCreateKalman(int dynam_params, int measure_params, int control_params=0) -> CvKalman"""
  return _cv.cvCreateKalman(*args)

def cvKalmanPredict(*args):
  """cvKalmanPredict(CvKalman kalman, CvMat control=None) -> CvMat"""
  return _cv.cvKalmanPredict(*args)

def cvKalmanCorrect(*args):
  """cvKalmanCorrect(CvKalman kalman, CvMat measurement) -> CvMat"""
  return _cv.cvKalmanCorrect(*args)

def cvInitSubdivDelaunay2D(*args):
  """cvInitSubdivDelaunay2D(CvSubdiv2D subdiv, CvRect rect)"""
  return _cv.cvInitSubdivDelaunay2D(*args)

def cvCreateSubdiv2D(*args):
  """
    cvCreateSubdiv2D(int subdiv_type, int header_size, int vtx_size, int quadedge_size, 
        CvMemStorage storage) -> CvSubdiv2D
    """
  return _cv.cvCreateSubdiv2D(*args)

def cvCreateSubdivDelaunay2D(*args):
  """cvCreateSubdivDelaunay2D(CvRect rect, CvMemStorage storage) -> CvSubdiv2D"""
  return _cv.cvCreateSubdivDelaunay2D(*args)

def cvSubdivDelaunay2DInsert(*args):
  """cvSubdivDelaunay2DInsert(CvSubdiv2D subdiv, CvPoint2D32f pt) -> CvSubdiv2DPoint"""
  return _cv.cvSubdivDelaunay2DInsert(*args)

def cvSubdiv2DLocate(*args):
  """cvSubdiv2DLocate(CvSubdiv2D subdiv, CvPoint2D32f pt, CvSubdiv2DEdge edge) -> int"""
  return _cv.cvSubdiv2DLocate(*args)

def cvCalcSubdivVoronoi2D(*args):
  """cvCalcSubdivVoronoi2D(CvSubdiv2D subdiv)"""
  return _cv.cvCalcSubdivVoronoi2D(*args)

def cvClearSubdivVoronoi2D(*args):
  """cvClearSubdivVoronoi2D(CvSubdiv2D subdiv)"""
  return _cv.cvClearSubdivVoronoi2D(*args)

def cvFindNearestPoint2D(*args):
  """cvFindNearestPoint2D(CvSubdiv2D subdiv, CvPoint2D32f pt) -> CvSubdiv2DPoint"""
  return _cv.cvFindNearestPoint2D(*args)

def cvSubdiv2DNextEdge(*args):
  """cvSubdiv2DNextEdge(CvSubdiv2DEdge edge) -> CvSubdiv2DEdge"""
  return _cv.cvSubdiv2DNextEdge(*args)

def cvSubdiv2DRotateEdge(*args):
  """cvSubdiv2DRotateEdge(CvSubdiv2DEdge edge, int rotate) -> CvSubdiv2DEdge"""
  return _cv.cvSubdiv2DRotateEdge(*args)

def cvSubdiv2DSymEdge(*args):
  """cvSubdiv2DSymEdge(CvSubdiv2DEdge edge) -> CvSubdiv2DEdge"""
  return _cv.cvSubdiv2DSymEdge(*args)

def cvSubdiv2DGetEdge(*args):
  """cvSubdiv2DGetEdge(CvSubdiv2DEdge edge, CvNextEdgeType type) -> CvSubdiv2DEdge"""
  return _cv.cvSubdiv2DGetEdge(*args)

def cvSubdiv2DEdgeOrg(*args):
  """cvSubdiv2DEdgeOrg(CvSubdiv2DEdge edge) -> CvSubdiv2DPoint"""
  return _cv.cvSubdiv2DEdgeOrg(*args)

def cvSubdiv2DEdgeDst(*args):
  """cvSubdiv2DEdgeDst(CvSubdiv2DEdge edge) -> CvSubdiv2DPoint"""
  return _cv.cvSubdiv2DEdgeDst(*args)

def cvTriangleArea(*args):
  """cvTriangleArea(CvPoint2D32f a, CvPoint2D32f b, CvPoint2D32f c) -> double"""
  return _cv.cvTriangleArea(*args)

def cvFindDominantPoints(*args):
  """
    cvFindDominantPoints(CvSeq contour, CvMemStorage storage, int method=1, 
        double parameter1=0, double parameter2=0, double parameter3=0, 
        double parameter4=0) -> CvSeq
    """
  return _cv.cvFindDominantPoints(*args)

def cvBoundingRect(*args):
  """cvBoundingRect(CvArr points, int update=0) -> CvRect"""
  return _cv.cvBoundingRect(*args)

def cvContourArea(*args):
  """cvContourArea(CvArr contour, CvSlice slice=cvSlice(0, 0x3fffffff)) -> double"""
  return _cv.cvContourArea(*args)

def cvMinAreaRect2(*args):
  """cvMinAreaRect2(CvArr points, CvMemStorage storage=None) -> CvBox2D"""
  return _cv.cvMinAreaRect2(*args)

def cvMinEnclosingCircle(*args):
  """cvMinEnclosingCircle(CvArr points, CvPoint2D32f center) -> int"""
  return _cv.cvMinEnclosingCircle(*args)

def cvMatchShapes(*args):
  """cvMatchShapes(void object1, void object2, int method, double parameter=0) -> double"""
  return _cv.cvMatchShapes(*args)

def cvCreateContourTree(*args):
  """cvCreateContourTree(CvSeq contour, CvMemStorage storage, double threshold) -> CvContourTree"""
  return _cv.cvCreateContourTree(*args)

def cvContourFromContourTreeUntyped(*args):
  """cvContourFromContourTreeUntyped(CvContourTree tree, CvMemStorage storage, CvTermCriteria criteria) -> CvSeq"""
  return _cv.cvContourFromContourTreeUntyped(*args)

def cvMatchContourTrees(*args):
  """
    cvMatchContourTrees(CvContourTree tree1, CvContourTree tree2, int method, 
        double threshold) -> double
    """
  return _cv.cvMatchContourTrees(*args)

def cvCalcPGH(*args):
  """cvCalcPGH(CvSeq contour, CvHistogram hist)"""
  return _cv.cvCalcPGH(*args)

def cvCheckContourConvexity(*args):
  """cvCheckContourConvexity(CvArr contour) -> int"""
  return _cv.cvCheckContourConvexity(*args)

def cvConvexityDefectsUntyped(*args):
  """cvConvexityDefectsUntyped(CvArr contour, CvArr convexhull, CvMemStorage storage=None) -> CvSeq"""
  return _cv.cvConvexityDefectsUntyped(*args)

def cvFitEllipse2(*args):
  """cvFitEllipse2(CvArr points) -> CvBox2D"""
  return _cv.cvFitEllipse2(*args)

def cvMaxRect(*args):
  """cvMaxRect(CvRect rect1, CvRect rect2) -> CvRect"""
  return _cv.cvMaxRect(*args)

def cvBoxPoints(*args):
  """cvBoxPoints(CvBox2D box, CvPoint2D32f pt)"""
  return _cv.cvBoxPoints(*args)

def cvPointSeqFromMat(*args):
  """
    cvPointSeqFromMat(int seq_kind, CvArr mat, CvContour contour_header, 
        CvSeqBlock block) -> CvSeq
    """
  return _cv.cvPointSeqFromMat(*args)

def cvPointPolygonTest(*args):
  """cvPointPolygonTest(CvArr contour, CvPoint2D32f pt, int measure_dist) -> double"""
  return _cv.cvPointPolygonTest(*args)

def cvCreateHist(*args):
  """cvCreateHist(int dims, int type, float ranges=None, int uniform=1) -> CvHistogram"""
  return _cv.cvCreateHist(*args)

def cvSetHistBinRanges(*args):
  """cvSetHistBinRanges(CvHistogram hist, float ranges, int uniform=1)"""
  return _cv.cvSetHistBinRanges(*args)

def cvMakeHistHeaderForArray(*args):
  """
    cvMakeHistHeaderForArray(int dims, CvHistogram hist, float data, float ranges=None, 
        int uniform=1) -> CvHistogram
    """
  return _cv.cvMakeHistHeaderForArray(*args)

def cvClearHist(*args):
  """cvClearHist(CvHistogram hist)"""
  return _cv.cvClearHist(*args)

def cvGetMinMaxHistValue(*args):
  """
    cvGetMinMaxHistValue(CvHistogram hist, float min_value, float max_value, 
        int min_idx=None, int max_idx=None)
    """
  return _cv.cvGetMinMaxHistValue(*args)

def cvNormalizeHist(*args):
  """cvNormalizeHist(CvHistogram hist, double factor)"""
  return _cv.cvNormalizeHist(*args)

def cvThreshHist(*args):
  """cvThreshHist(CvHistogram hist, double threshold)"""
  return _cv.cvThreshHist(*args)

def cvCompareHist(*args):
  """cvCompareHist(CvHistogram hist1, CvHistogram hist2, int method) -> double"""
  return _cv.cvCompareHist(*args)

def cvCopyHist(*args):
  """cvCopyHist(CvHistogram src, CvHistogram dst)"""
  return _cv.cvCopyHist(*args)

def cvCalcBayesianProb(*args):
  """cvCalcBayesianProb(CvHistogram src, int number, CvHistogram dst)"""
  return _cv.cvCalcBayesianProb(*args)

def cvCalcArrHist(*args):
  """cvCalcArrHist(CvArr arr, CvHistogram hist, int accumulate=0, CvArr mask=None)"""
  return _cv.cvCalcArrHist(*args)

def cvCalcImageHist(*args):
  """cvCalcImageHist( image, CvHistogram hist, int accumulate=0, CvArr mask=None)"""
  return _cv.cvCalcImageHist(*args)

def cvCalcArrBackProject(*args):
  """cvCalcArrBackProject(CvArr image, CvArr dst, CvHistogram hist)"""
  return _cv.cvCalcArrBackProject(*args)

def cvCalcArrBackProjectPatch(*args):
  """
    cvCalcArrBackProjectPatch(CvArr image, CvArr dst, CvSize range, CvHistogram hist, 
        int method, double factor)
    """
  return _cv.cvCalcArrBackProjectPatch(*args)

def cvCalcProbDensity(*args):
  """
    cvCalcProbDensity(CvHistogram hist1, CvHistogram hist2, CvHistogram dst_hist, 
        double scale=255)
    """
  return _cv.cvCalcProbDensity(*args)

def cvEqualizeHist(*args):
  """cvEqualizeHist(CvArr src, CvArr dst)"""
  return _cv.cvEqualizeHist(*args)

def cvSnakeImage(*args):
  """
    cvSnakeImage( image, CvPoint points, int length, float alpha, float beta, 
        float gamma, int coeff_usage, CvSize win, 
        CvTermCriteria criteria, int calc_gradient=1)
    """
  return _cv.cvSnakeImage(*args)

def cvCalcImageHomography(*args):
  """cvCalcImageHomography(float line, CvPoint3D32f center, float intrinsic, float homography)"""
  return _cv.cvCalcImageHomography(*args)

def cvDistTransform(*args):
  """
    cvDistTransform(CvArr src, CvArr dst, int distance_type=2, int mask_size=3, 
        float mask=None, CvArr labels=None)
    """
  return _cv.cvDistTransform(*args)

def cvThreshold(*args):
  """
    cvThreshold(CvArr src, CvArr dst, double threshold, double max_value, 
        int threshold_type)
    """
  return _cv.cvThreshold(*args)

def cvAdaptiveThreshold(*args):
  """
    cvAdaptiveThreshold(CvArr src, CvArr dst, double max_value, int adaptive_method=0, 
        int threshold_type=0, int block_size=3, 
        double param1=5)
    """
  return _cv.cvAdaptiveThreshold(*args)

def cvFloodFill(*args):
  """
    cvFloodFill(CvArr image, CvPoint seed_point, CvScalar new_val, 
        CvScalar lo_diff=cvScalarAll(0), CvScalar up_diff=cvScalarAll(0), 
        CvConnectedComp comp=None, 
        int flags=4, CvArr mask=None)
    """
  return _cv.cvFloodFill(*args)

def cvCanny(*args):
  """
    cvCanny(CvArr image, CvArr edges, double threshold1, double threshold2, 
        int aperture_size=3)
    """
  return _cv.cvCanny(*args)

def cvPreCornerDetect(*args):
  """cvPreCornerDetect(CvArr image, CvArr corners, int aperture_size=3)"""
  return _cv.cvPreCornerDetect(*args)

def cvCornerEigenValsAndVecs(*args):
  """cvCornerEigenValsAndVecs(CvArr image, CvArr eigenvv, int block_size, int aperture_size=3)"""
  return _cv.cvCornerEigenValsAndVecs(*args)

def cvCornerMinEigenVal(*args):
  """cvCornerMinEigenVal(CvArr image, CvArr eigenval, int block_size, int aperture_size=3)"""
  return _cv.cvCornerMinEigenVal(*args)

def cvCornerHarris(*args):
  """
    cvCornerHarris(CvArr image, CvArr harris_responce, int block_size, 
        int aperture_size=3, double k=0.04)
    """
  return _cv.cvCornerHarris(*args)

def cvFindCornerSubPix(*args):
  """
    cvFindCornerSubPix(CvArr image, CvPoint2D32f corners, CvSize win, CvSize zero_zone, 
        CvTermCriteria criteria)
    """
  return _cv.cvFindCornerSubPix(*args)

def cvGoodFeaturesToTrack(*args):
  """
    cvGoodFeaturesToTrack(CvArr image, CvArr eig_image, CvArr temp_image, CvPoint2D32f corners, 
        double quality_level, double min_distance, 
        CvArr mask=None, int block_size=3, 
        int use_harris=0, double k=0.04)
    """
  return _cv.cvGoodFeaturesToTrack(*args)

def cvHoughLinesUntyped(*args):
  """
    cvHoughLinesUntyped(CvArr image, void line_storage, int method, double rho, 
        double theta, int threshold, double param1=0, 
        double param2=0) -> CvSeq
    """
  return _cv.cvHoughLinesUntyped(*args)

def cvHoughCirclesUntyped(*args):
  """
    cvHoughCirclesUntyped(CvArr image, void circle_storage, int method, double dp, 
        double min_dist, double param1=100, double param2=100, 
        int min_radius=0, int max_radius=0) -> CvSeq
    """
  return _cv.cvHoughCirclesUntyped(*args)

def cvFitLine(*args):
  """
    cvFitLine(CvArr points, int dist_type, double param, double reps, 
        double aeps, float line)
    """
  return _cv.cvFitLine(*args)

def cvLoadHaarClassifierCascade(*args):
  """cvLoadHaarClassifierCascade(char directory, CvSize orig_window_size) -> CvHaarClassifierCascade"""
  return _cv.cvLoadHaarClassifierCascade(*args)

def cvSetImagesForHaarClassifierCascade(*args):
  """
    cvSetImagesForHaarClassifierCascade(CvHaarClassifierCascade cascade, CvArr sum, CvArr sqsum, 
        CvArr tilted_sum, double scale)
    """
  return _cv.cvSetImagesForHaarClassifierCascade(*args)

def cvRunHaarClassifierCascade(*args):
  """cvRunHaarClassifierCascade(CvHaarClassifierCascade cascade, CvPoint pt, int start_stage=0) -> int"""
  return _cv.cvRunHaarClassifierCascade(*args)

def cvUndistort2(*args):
  """cvUndistort2(CvArr src, CvArr dst, CvMat intrinsic_matrix, CvMat distortion_coeffs)"""
  return _cv.cvUndistort2(*args)

def cvInitUndistortMap(*args):
  """
    cvInitUndistortMap(CvMat intrinsic_matrix, CvMat distortion_coeffs, CvArr mapx, 
        CvArr mapy)
    """
  return _cv.cvInitUndistortMap(*args)

def cvRodrigues2(*args):
  """cvRodrigues2(CvMat src, CvMat dst, CvMat jacobian=0) -> int"""
  return _cv.cvRodrigues2(*args)

def cvFindHomography(*args):
  """cvFindHomography(CvMat src_points, CvMat dst_points, CvMat homography)"""
  return _cv.cvFindHomography(*args)

def cvProjectPoints2(*args):
  """
    cvProjectPoints2(CvMat object_points, CvMat rotation_vector, CvMat translation_vector, 
        CvMat intrinsic_matrix, CvMat distortion_coeffs, 
        CvMat image_points, CvMat dpdrot=None, 
        CvMat dpdt=None, CvMat dpdf=None, 
        CvMat dpdc=None, CvMat dpddist=None)
    """
  return _cv.cvProjectPoints2(*args)

def cvFindExtrinsicCameraParams2(*args):
  """
    cvFindExtrinsicCameraParams2(CvMat object_points, CvMat image_points, CvMat intrinsic_matrix, 
        CvMat distortion_coeffs, CvMat rotation_vector, 
        CvMat translation_vector)
    """
  return _cv.cvFindExtrinsicCameraParams2(*args)

def cvCalibrateCamera2(*args):
  """
    cvCalibrateCamera2(CvMat object_points, CvMat image_points, CvMat point_counts, 
        CvSize image_size, CvMat intrinsic_matrix, 
        CvMat rotation_vectors=None, CvMat translation_vectors=None, 
        int flags=0)
    """
  return _cv.cvCalibrateCamera2(*args)

def cvFindChessboardCorners(*args):
  """cvFindChessboardCorners(void image, CvSize pattern_size, int flags=1) -> int"""
  return _cv.cvFindChessboardCorners(*args)

def cvDrawChessboardCorners(*args):
  """
    cvDrawChessboardCorners(CvArr image, CvSize pattern_size, CvPoint2D32f corners, 
        int pattern_was_found)
    """
  return _cv.cvDrawChessboardCorners(*args)

def cvCreatePOSITObject(*args):
  """cvCreatePOSITObject(CvPoint3D32f points, int point_count) -> CvPOSITObject"""
  return _cv.cvCreatePOSITObject(*args)

def cvPOSIT(*args):
  """
    cvPOSIT(CvPOSITObject posit_object, CvPoint2D32f image_points, 
        double focal_length, CvTermCriteria criteria, 
        CvMatr32f rotation_matrix, CvVect32f translation_vector)
    """
  return _cv.cvPOSIT(*args)

def cvConvertPointsHomogenious(*args):
  """cvConvertPointsHomogenious(CvMat src, CvMat dst)"""
  return _cv.cvConvertPointsHomogenious(*args)

def cvFindFundamentalMat(*args):
  """
    cvFindFundamentalMat(CvMat points1, CvMat points2, CvMat fundamental_matrix, 
        int method=(8+2), double param1=1., double param2=0.99, 
        CvMat status=None) -> int
    """
  return _cv.cvFindFundamentalMat(*args)

def cvComputeCorrespondEpilines(*args):
  """
    cvComputeCorrespondEpilines(CvMat points, int which_image, CvMat fundamental_matrix, 
        CvMat correspondent_lines)
    """
  return _cv.cvComputeCorrespondEpilines(*args)
class CvBaseImageFilter(_object):
    """Proxy of C++ CvBaseImageFilter class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvBaseImageFilter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvBaseImageFilter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvBaseImageFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0)) -> CvBaseImageFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1) -> CvBaseImageFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1)) -> CvBaseImageFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize) -> CvBaseImageFilter
        """
        this = _cv.new_CvBaseImageFilter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvBaseImageFilter
    __del__ = lambda self : None;
    def init(*args):
        """
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize)
        """
        return _cv.CvBaseImageFilter_init(*args)

    def clear(*args):
        """clear(self)"""
        return _cv.CvBaseImageFilter_clear(*args)

    def process(*args):
        """
        process(self, CvMat _src, CvMat _dst, CvRect _src_roi=cvRect(0,0,-1,-1), 
            CvPoint _dst_origin=cvPoint(0,0), int _flags=0) -> int
        process(self, CvMat _src, CvMat _dst, CvRect _src_roi=cvRect(0,0,-1,-1), 
            CvPoint _dst_origin=cvPoint(0,0)) -> int
        process(self, CvMat _src, CvMat _dst, CvRect _src_roi=cvRect(0,0,-1,-1)) -> int
        process(self, CvMat _src, CvMat _dst) -> int
        """
        return _cv.CvBaseImageFilter_process(*args)

    def get_src_type(*args):
        """get_src_type(self) -> int"""
        return _cv.CvBaseImageFilter_get_src_type(*args)

    def get_dst_type(*args):
        """get_dst_type(self) -> int"""
        return _cv.CvBaseImageFilter_get_dst_type(*args)

    def get_work_type(*args):
        """get_work_type(self) -> int"""
        return _cv.CvBaseImageFilter_get_work_type(*args)

    def get_kernel_size(*args):
        """get_kernel_size(self) -> CvSize"""
        return _cv.CvBaseImageFilter_get_kernel_size(*args)

    def get_anchor(*args):
        """get_anchor(self) -> CvPoint"""
        return _cv.CvBaseImageFilter_get_anchor(*args)

    def get_width(*args):
        """get_width(self) -> int"""
        return _cv.CvBaseImageFilter_get_width(*args)

    def get_x_filter_func(*args):
        """get_x_filter_func(self) -> CvRowFilterFunc"""
        return _cv.CvBaseImageFilter_get_x_filter_func(*args)

    def get_y_filter_func(*args):
        """get_y_filter_func(self) -> CvColumnFilterFunc"""
        return _cv.CvBaseImageFilter_get_y_filter_func(*args)

CvBaseImageFilter_swigregister = _cv.CvBaseImageFilter_swigregister
CvBaseImageFilter_swigregister(CvBaseImageFilter)

class CvSepFilter(CvBaseImageFilter):
    """Proxy of C++ CvSepFilter class"""
    __swig_setmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSepFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSepFilter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvSepFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0)) -> CvSepFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1) -> CvSepFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1)) -> CvSepFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky) -> CvSepFilter
        """
        this = _cv.new_CvSepFilter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSepFilter
    __del__ = lambda self : None;
    def init_deriv(*args):
        """
        init_deriv(self, int _max_width, int _src_type, int _dst_type, int dx, 
            int dy, int aperture_size, int flags=0)
        init_deriv(self, int _max_width, int _src_type, int _dst_type, int dx, 
            int dy, int aperture_size)
        """
        return _cv.CvSepFilter_init_deriv(*args)

    def init_gaussian(*args):
        """
        init_gaussian(self, int _max_width, int _src_type, int _dst_type, int gaussian_size, 
            double sigma)
        """
        return _cv.CvSepFilter_init_gaussian(*args)

    def init(*args):
        """
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize)
        """
        return _cv.CvSepFilter_init(*args)

    def clear(*args):
        """clear(self)"""
        return _cv.CvSepFilter_clear(*args)

    def get_x_kernel(*args):
        """get_x_kernel(self) -> CvMat"""
        return _cv.CvSepFilter_get_x_kernel(*args)

    def get_y_kernel(*args):
        """get_y_kernel(self) -> CvMat"""
        return _cv.CvSepFilter_get_y_kernel(*args)

    def get_x_kernel_flags(*args):
        """get_x_kernel_flags(self) -> int"""
        return _cv.CvSepFilter_get_x_kernel_flags(*args)

    def get_y_kernel_flags(*args):
        """get_y_kernel_flags(self) -> int"""
        return _cv.CvSepFilter_get_y_kernel_flags(*args)

    GENERIC = _cv.CvSepFilter_GENERIC
    ASYMMETRICAL = _cv.CvSepFilter_ASYMMETRICAL
    SYMMETRICAL = _cv.CvSepFilter_SYMMETRICAL
    POSITIVE = _cv.CvSepFilter_POSITIVE
    SUM_TO_1 = _cv.CvSepFilter_SUM_TO_1
    INTEGER = _cv.CvSepFilter_INTEGER
    NORMALIZE_KERNEL = _cv.CvSepFilter_NORMALIZE_KERNEL
    FLIP_KERNEL = _cv.CvSepFilter_FLIP_KERNEL
    def init_gaussian_kernel(*args):
        """
        init_gaussian_kernel(CvMat kernel, double sigma=-1)
        init_gaussian_kernel(CvMat kernel)
        """
        return _cv.CvSepFilter_init_gaussian_kernel(*args)

    if _newclass:init_gaussian_kernel = staticmethod(init_gaussian_kernel)
    __swig_getmethods__["init_gaussian_kernel"] = lambda x: init_gaussian_kernel
    def init_sobel_kernel(*args):
        """
        init_sobel_kernel(CvMat _kx, CvMat _ky, int dx, int dy, int flags=0)
        init_sobel_kernel(CvMat _kx, CvMat _ky, int dx, int dy)
        """
        return _cv.CvSepFilter_init_sobel_kernel(*args)

    if _newclass:init_sobel_kernel = staticmethod(init_sobel_kernel)
    __swig_getmethods__["init_sobel_kernel"] = lambda x: init_sobel_kernel
    def init_scharr_kernel(*args):
        """
        init_scharr_kernel(CvMat _kx, CvMat _ky, int dx, int dy, int flags=0)
        init_scharr_kernel(CvMat _kx, CvMat _ky, int dx, int dy)
        """
        return _cv.CvSepFilter_init_scharr_kernel(*args)

    if _newclass:init_scharr_kernel = staticmethod(init_scharr_kernel)
    __swig_getmethods__["init_scharr_kernel"] = lambda x: init_scharr_kernel
CvSepFilter_swigregister = _cv.CvSepFilter_swigregister
CvSepFilter_swigregister(CvSepFilter)

def CvSepFilter_init_gaussian_kernel(*args):
  """
    init_gaussian_kernel(CvMat kernel, double sigma=-1)
    CvSepFilter_init_gaussian_kernel(CvMat kernel)
    """
  return _cv.CvSepFilter_init_gaussian_kernel(*args)

def CvSepFilter_init_sobel_kernel(*args):
  """
    init_sobel_kernel(CvMat _kx, CvMat _ky, int dx, int dy, int flags=0)
    CvSepFilter_init_sobel_kernel(CvMat _kx, CvMat _ky, int dx, int dy)
    """
  return _cv.CvSepFilter_init_sobel_kernel(*args)

def CvSepFilter_init_scharr_kernel(*args):
  """
    init_scharr_kernel(CvMat _kx, CvMat _ky, int dx, int dy, int flags=0)
    CvSepFilter_init_scharr_kernel(CvMat _kx, CvMat _ky, int dx, int dy)
    """
  return _cv.CvSepFilter_init_scharr_kernel(*args)

class CvLinearFilter(CvBaseImageFilter):
    """Proxy of C++ CvLinearFilter class"""
    __swig_setmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvLinearFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvLinearFilter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvLinearFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel, 
            CvPoint _anchor=cvPoint(-1,-1), int _border_mode=1, 
            CvScalar _border_value=cvScalarAll(0)) -> CvLinearFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel, 
            CvPoint _anchor=cvPoint(-1,-1), int _border_mode=1) -> CvLinearFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel, 
            CvPoint _anchor=cvPoint(-1,-1)) -> CvLinearFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel) -> CvLinearFilter
        """
        this = _cv.new_CvLinearFilter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvLinearFilter
    __del__ = lambda self : None;
    def init(*args):
        """
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel, 
            CvPoint _anchor=cvPoint(-1,-1), int _border_mode=1, 
            CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel, 
            CvPoint _anchor=cvPoint(-1,-1), int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel, 
            CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kernel)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize)
        """
        return _cv.CvLinearFilter_init(*args)

    def clear(*args):
        """clear(self)"""
        return _cv.CvLinearFilter_clear(*args)

    def get_kernel(*args):
        """get_kernel(self) -> CvMat"""
        return _cv.CvLinearFilter_get_kernel(*args)

    def get_kernel_sparse_buf(*args):
        """get_kernel_sparse_buf(self) -> uchar"""
        return _cv.CvLinearFilter_get_kernel_sparse_buf(*args)

    def get_kernel_sparse_count(*args):
        """get_kernel_sparse_count(self) -> int"""
        return _cv.CvLinearFilter_get_kernel_sparse_count(*args)

CvLinearFilter_swigregister = _cv.CvLinearFilter_swigregister
CvLinearFilter_swigregister(CvLinearFilter)

class CvBoxFilter(CvBaseImageFilter):
    """Proxy of C++ CvBoxFilter class"""
    __swig_setmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvBoxFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvBoxFilter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvBoxFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0)) -> CvBoxFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1) -> CvBoxFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1)) -> CvBoxFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize) -> CvBoxFilter
        """
        this = _cv.new_CvBoxFilter(*args)
        try: self.this.append(this)
        except: self.this = this
    def init(*args):
        """
        init(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            CvSize _ksize)
        """
        return _cv.CvBoxFilter_init(*args)

    __swig_destroy__ = _cv.delete_CvBoxFilter
    __del__ = lambda self : None;
    def is_normalized(*args):
        """is_normalized(self) -> bool"""
        return _cv.CvBoxFilter_is_normalized(*args)

    def get_scale(*args):
        """get_scale(self) -> double"""
        return _cv.CvBoxFilter_get_scale(*args)

    def get_sum_buf(*args):
        """get_sum_buf(self) -> uchar"""
        return _cv.CvBoxFilter_get_sum_buf(*args)

    def get_sum_count_ptr(*args):
        """get_sum_count_ptr(self) -> int"""
        return _cv.CvBoxFilter_get_sum_count_ptr(*args)

CvBoxFilter_swigregister = _cv.CvBoxFilter_swigregister
CvBoxFilter_swigregister(CvBoxFilter)

class CvLaplaceFilter(CvSepFilter):
    """Proxy of C++ CvLaplaceFilter class"""
    __swig_setmethods__ = {}
    for _s in [CvSepFilter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvLaplaceFilter, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSepFilter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvLaplaceFilter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvLaplaceFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            int _ksize, int _border_mode=1, 
            CvScalar _border_value=cvScalarAll(0)) -> CvLaplaceFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            int _ksize, int _border_mode=1) -> CvLaplaceFilter
        __init__(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            int _ksize) -> CvLaplaceFilter
        """
        this = _cv.new_CvLaplaceFilter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvLaplaceFilter
    __del__ = lambda self : None;
    def init(*args):
        """
        init(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            int _ksize, int _border_mode=1, 
            CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            int _ksize, int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, bool _normalized, 
            int _ksize)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize)
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, CvMat _kx, 
            CvMat _ky)
        """
        return _cv.CvLaplaceFilter_init(*args)

    def is_normalized(*args):
        """is_normalized(self) -> bool"""
        return _cv.CvLaplaceFilter_is_normalized(*args)

    def is_basic_laplacian(*args):
        """is_basic_laplacian(self) -> bool"""
        return _cv.CvLaplaceFilter_is_basic_laplacian(*args)

CvLaplaceFilter_swigregister = _cv.CvLaplaceFilter_swigregister
CvLaplaceFilter_swigregister(CvLaplaceFilter)

class CvMorphology(CvBaseImageFilter):
    """Proxy of C++ CvMorphology class"""
    __swig_setmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvMorphology, name, value)
    __swig_getmethods__ = {}
    for _s in [CvBaseImageFilter]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvMorphology, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> CvMorphology
        __init__(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0), 
            CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0)) -> CvMorphology
        __init__(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0), 
            CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1) -> CvMorphology
        __init__(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0), 
            CvPoint _anchor=cvPoint(-1,-1)) -> CvMorphology
        __init__(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0)) -> CvMorphology
        __init__(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element) -> CvMorphology
        """
        this = _cv.new_CvMorphology(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvMorphology
    __del__ = lambda self : None;
    def init(*args):
        """
        init(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0), 
            CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0), 
            CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0), 
            CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element, CvSize _ksize=cvSize(0,0))
        init(self, int _operation, int _max_width, int _src_dst_type, 
            int _element_shape, CvMat _element)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1, CvScalar _border_value=cvScalarAll(0))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1), 
            int _border_mode=1)
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize, CvPoint _anchor=cvPoint(-1,-1))
        init(self, int _max_width, int _src_type, int _dst_type, bool _is_separable, 
            CvSize _ksize)
        """
        return _cv.CvMorphology_init(*args)

    def clear(*args):
        """clear(self)"""
        return _cv.CvMorphology_clear(*args)

    def get_element(*args):
        """get_element(self) -> CvMat"""
        return _cv.CvMorphology_get_element(*args)

    def get_element_shape(*args):
        """get_element_shape(self) -> int"""
        return _cv.CvMorphology_get_element_shape(*args)

    def get_operation(*args):
        """get_operation(self) -> int"""
        return _cv.CvMorphology_get_operation(*args)

    def get_element_sparse_buf(*args):
        """get_element_sparse_buf(self) -> uchar"""
        return _cv.CvMorphology_get_element_sparse_buf(*args)

    def get_element_sparse_count(*args):
        """get_element_sparse_count(self) -> int"""
        return _cv.CvMorphology_get_element_sparse_count(*args)

    RECT = _cv.CvMorphology_RECT
    CROSS = _cv.CvMorphology_CROSS
    ELLIPSE = _cv.CvMorphology_ELLIPSE
    CUSTOM = _cv.CvMorphology_CUSTOM
    BINARY = _cv.CvMorphology_BINARY
    GRAYSCALE = _cv.CvMorphology_GRAYSCALE
    ERODE = _cv.CvMorphology_ERODE
    DILATE = _cv.CvMorphology_DILATE
    def init_binary_element(*args):
        """
        init_binary_element(CvMat _element, int _element_shape, CvPoint _anchor=cvPoint(-1,-1))
        init_binary_element(CvMat _element, int _element_shape)
        """
        return _cv.CvMorphology_init_binary_element(*args)

    if _newclass:init_binary_element = staticmethod(init_binary_element)
    __swig_getmethods__["init_binary_element"] = lambda x: init_binary_element
CvMorphology_swigregister = _cv.CvMorphology_swigregister
CvMorphology_swigregister(CvMorphology)

def CvMorphology_init_binary_element(*args):
  """
    init_binary_element(CvMat _element, int _element_shape, CvPoint _anchor=cvPoint(-1,-1))
    CvMorphology_init_binary_element(CvMat _element, int _element_shape)
    """
  return _cv.CvMorphology_init_binary_element(*args)

class CvTuple_CvPoint_2(_object):
    """Proxy of C++ CvTuple_CvPoint_2 class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvTuple_CvPoint_2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvTuple_CvPoint_2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["val"] = _cv.CvTuple_CvPoint_2_val_set
    __swig_getmethods__["val"] = _cv.CvTuple_CvPoint_2_val_get
    if _newclass:val = _swig_property(_cv.CvTuple_CvPoint_2_val_get, _cv.CvTuple_CvPoint_2_val_set)
    def __setitem__(*args):
        """__setitem__(self, int i, CvPoint obj)"""
        return _cv.CvTuple_CvPoint_2___setitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, int i) -> CvPoint"""
        return _cv.CvTuple_CvPoint_2___getitem__(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvTuple_CvPoint_2"""
        this = _cv.new_CvTuple_CvPoint_2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvTuple_CvPoint_2
    __del__ = lambda self : None;
CvTuple_CvPoint_2_swigregister = _cv.CvTuple_CvPoint_2_swigregister
CvTuple_CvPoint_2_swigregister(CvTuple_CvPoint_2)

class CvTuple_float_2(_object):
    """Proxy of C++ CvTuple_float_2 class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvTuple_float_2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvTuple_float_2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["val"] = _cv.CvTuple_float_2_val_set
    __swig_getmethods__["val"] = _cv.CvTuple_float_2_val_get
    if _newclass:val = _swig_property(_cv.CvTuple_float_2_val_get, _cv.CvTuple_float_2_val_set)
    def __setitem__(*args):
        """__setitem__(self, int i, float obj)"""
        return _cv.CvTuple_float_2___setitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, int i) -> float"""
        return _cv.CvTuple_float_2___getitem__(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvTuple_float_2"""
        this = _cv.new_CvTuple_float_2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvTuple_float_2
    __del__ = lambda self : None;
CvTuple_float_2_swigregister = _cv.CvTuple_float_2_swigregister
CvTuple_float_2_swigregister(CvTuple_float_2)

class CvTuple_float_3(_object):
    """Proxy of C++ CvTuple_float_3 class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvTuple_float_3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CvTuple_float_3, name)
    __repr__ = _swig_repr
    __swig_setmethods__["val"] = _cv.CvTuple_float_3_val_set
    __swig_getmethods__["val"] = _cv.CvTuple_float_3_val_get
    if _newclass:val = _swig_property(_cv.CvTuple_float_3_val_get, _cv.CvTuple_float_3_val_set)
    def __setitem__(*args):
        """__setitem__(self, int i, float obj)"""
        return _cv.CvTuple_float_3___setitem__(*args)

    def __getitem__(*args):
        """__getitem__(self, int i) -> float"""
        return _cv.CvTuple_float_3___getitem__(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvTuple_float_3"""
        this = _cv.new_CvTuple_float_3(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvTuple_float_3
    __del__ = lambda self : None;
CvTuple_float_3_swigregister = _cv.CvTuple_float_3_swigregister
CvTuple_float_3_swigregister(CvTuple_float_3)

class CvSeq_CvPoint(CvSeq):
    """Proxy of C++ CvSeq_CvPoint class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_CvPoint, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_CvPoint, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_CvPoint"""
        return _cv.CvSeq_CvPoint_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvPoint"""
        return _cv.CvSeq_CvPoint___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvPoint obj)"""
        return _cv.CvSeq_CvPoint___setitem__(*args)

    def append(*args):
        """append(self, CvPoint obj)"""
        return _cv.CvSeq_CvPoint_append(*args)

    def pop(*args):
        """pop(self) -> CvPoint"""
        return _cv.CvSeq_CvPoint_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_CvPoint"""
        this = _cv.new_CvSeq_CvPoint(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_CvPoint
    __del__ = lambda self : None;
CvSeq_CvPoint_swigregister = _cv.CvSeq_CvPoint_swigregister
CvSeq_CvPoint_swigregister(CvSeq_CvPoint)

def CvSeq_CvPoint_cast(*args):
  """CvSeq_CvPoint_cast(CvSeq seq) -> CvSeq_CvPoint"""
  return _cv.CvSeq_CvPoint_cast(*args)

class CvSeq_CvPoint2D32f(CvSeq):
    """Proxy of C++ CvSeq_CvPoint2D32f class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_CvPoint2D32f, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_CvPoint2D32f, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_CvPoint2D32f"""
        return _cv.CvSeq_CvPoint2D32f_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvPoint2D32f"""
        return _cv.CvSeq_CvPoint2D32f___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvPoint2D32f obj)"""
        return _cv.CvSeq_CvPoint2D32f___setitem__(*args)

    def append(*args):
        """append(self, CvPoint2D32f obj)"""
        return _cv.CvSeq_CvPoint2D32f_append(*args)

    def pop(*args):
        """pop(self) -> CvPoint2D32f"""
        return _cv.CvSeq_CvPoint2D32f_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_CvPoint2D32f"""
        this = _cv.new_CvSeq_CvPoint2D32f(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_CvPoint2D32f
    __del__ = lambda self : None;
CvSeq_CvPoint2D32f_swigregister = _cv.CvSeq_CvPoint2D32f_swigregister
CvSeq_CvPoint2D32f_swigregister(CvSeq_CvPoint2D32f)

def CvSeq_CvPoint2D32f_cast(*args):
  """CvSeq_CvPoint2D32f_cast(CvSeq seq) -> CvSeq_CvPoint2D32f"""
  return _cv.CvSeq_CvPoint2D32f_cast(*args)

class CvSeq_CvRect(CvSeq):
    """Proxy of C++ CvSeq_CvRect class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_CvRect, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_CvRect, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_CvRect"""
        return _cv.CvSeq_CvRect_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvRect"""
        return _cv.CvSeq_CvRect___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvRect obj)"""
        return _cv.CvSeq_CvRect___setitem__(*args)

    def append(*args):
        """append(self, CvRect obj)"""
        return _cv.CvSeq_CvRect_append(*args)

    def pop(*args):
        """pop(self) -> CvRect"""
        return _cv.CvSeq_CvRect_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_CvRect"""
        this = _cv.new_CvSeq_CvRect(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_CvRect
    __del__ = lambda self : None;
CvSeq_CvRect_swigregister = _cv.CvSeq_CvRect_swigregister
CvSeq_CvRect_swigregister(CvSeq_CvRect)

def CvSeq_CvRect_cast(*args):
  """CvSeq_CvRect_cast(CvSeq seq) -> CvSeq_CvRect"""
  return _cv.CvSeq_CvRect_cast(*args)

class CvSeq_CvSeq(CvSeq):
    """Proxy of C++ CvSeq_CvSeq class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_CvSeq, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_CvSeq, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_CvSeq"""
        return _cv.CvSeq_CvSeq_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvSeq"""
        return _cv.CvSeq_CvSeq___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvSeq obj)"""
        return _cv.CvSeq_CvSeq___setitem__(*args)

    def append(*args):
        """append(self, CvSeq obj)"""
        return _cv.CvSeq_CvSeq_append(*args)

    def pop(*args):
        """pop(self) -> CvSeq"""
        return _cv.CvSeq_CvSeq_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_CvSeq"""
        this = _cv.new_CvSeq_CvSeq(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_CvSeq
    __del__ = lambda self : None;
CvSeq_CvSeq_swigregister = _cv.CvSeq_CvSeq_swigregister
CvSeq_CvSeq_swigregister(CvSeq_CvSeq)

def CvSeq_CvSeq_cast(*args):
  """CvSeq_CvSeq_cast(CvSeq seq) -> CvSeq_CvSeq"""
  return _cv.CvSeq_CvSeq_cast(*args)

class CvSeq_CvQuadEdge2D(CvSeq):
    """Proxy of C++ CvSeq_CvQuadEdge2D class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_CvQuadEdge2D, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_CvQuadEdge2D, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_CvQuadEdge2D"""
        return _cv.CvSeq_CvQuadEdge2D_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvQuadEdge2D"""
        return _cv.CvSeq_CvQuadEdge2D___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvQuadEdge2D obj)"""
        return _cv.CvSeq_CvQuadEdge2D___setitem__(*args)

    def append(*args):
        """append(self, CvQuadEdge2D obj)"""
        return _cv.CvSeq_CvQuadEdge2D_append(*args)

    def pop(*args):
        """pop(self) -> CvQuadEdge2D"""
        return _cv.CvSeq_CvQuadEdge2D_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_CvQuadEdge2D"""
        this = _cv.new_CvSeq_CvQuadEdge2D(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_CvQuadEdge2D
    __del__ = lambda self : None;
CvSeq_CvQuadEdge2D_swigregister = _cv.CvSeq_CvQuadEdge2D_swigregister
CvSeq_CvQuadEdge2D_swigregister(CvSeq_CvQuadEdge2D)

def CvSeq_CvQuadEdge2D_cast(*args):
  """CvSeq_CvQuadEdge2D_cast(CvSeq seq) -> CvSeq_CvQuadEdge2D"""
  return _cv.CvSeq_CvQuadEdge2D_cast(*args)

class CvSeq_CvConnectedComp(CvSeq):
    """Proxy of C++ CvSeq_CvConnectedComp class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_CvConnectedComp, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_CvConnectedComp, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_CvConnectedComp"""
        return _cv.CvSeq_CvConnectedComp_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvConnectedComp"""
        return _cv.CvSeq_CvConnectedComp___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvConnectedComp obj)"""
        return _cv.CvSeq_CvConnectedComp___setitem__(*args)

    def append(*args):
        """append(self, CvConnectedComp obj)"""
        return _cv.CvSeq_CvConnectedComp_append(*args)

    def pop(*args):
        """pop(self) -> CvConnectedComp"""
        return _cv.CvSeq_CvConnectedComp_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_CvConnectedComp"""
        this = _cv.new_CvSeq_CvConnectedComp(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_CvConnectedComp
    __del__ = lambda self : None;
CvSeq_CvConnectedComp_swigregister = _cv.CvSeq_CvConnectedComp_swigregister
CvSeq_CvConnectedComp_swigregister(CvSeq_CvConnectedComp)

def CvSeq_CvConnectedComp_cast(*args):
  """CvSeq_CvConnectedComp_cast(CvSeq seq) -> CvSeq_CvConnectedComp"""
  return _cv.CvSeq_CvConnectedComp_cast(*args)

class CvSeq_CvPoint_2(CvSeq):
    """Proxy of C++ CvSeq_CvPoint_2 class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_CvPoint_2, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_CvPoint_2, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_CvPoint_2"""
        return _cv.CvSeq_CvPoint_2_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvTuple_CvPoint_2"""
        return _cv.CvSeq_CvPoint_2___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvTuple_CvPoint_2 obj)"""
        return _cv.CvSeq_CvPoint_2___setitem__(*args)

    def append(*args):
        """append(self, CvTuple_CvPoint_2 obj)"""
        return _cv.CvSeq_CvPoint_2_append(*args)

    def pop(*args):
        """pop(self) -> CvTuple_CvPoint_2"""
        return _cv.CvSeq_CvPoint_2_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_CvPoint_2"""
        this = _cv.new_CvSeq_CvPoint_2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_CvPoint_2
    __del__ = lambda self : None;
CvSeq_CvPoint_2_swigregister = _cv.CvSeq_CvPoint_2_swigregister
CvSeq_CvPoint_2_swigregister(CvSeq_CvPoint_2)

def CvSeq_CvPoint_2_cast(*args):
  """CvSeq_CvPoint_2_cast(CvSeq seq) -> CvSeq_CvPoint_2"""
  return _cv.CvSeq_CvPoint_2_cast(*args)

class CvSeq_float_2(CvSeq):
    """Proxy of C++ CvSeq_float_2 class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_float_2, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_float_2, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_float_2"""
        return _cv.CvSeq_float_2_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvTuple_float_2"""
        return _cv.CvSeq_float_2___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvTuple_float_2 obj)"""
        return _cv.CvSeq_float_2___setitem__(*args)

    def append(*args):
        """append(self, CvTuple_float_2 obj)"""
        return _cv.CvSeq_float_2_append(*args)

    def pop(*args):
        """pop(self) -> CvTuple_float_2"""
        return _cv.CvSeq_float_2_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_float_2"""
        this = _cv.new_CvSeq_float_2(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_float_2
    __del__ = lambda self : None;
CvSeq_float_2_swigregister = _cv.CvSeq_float_2_swigregister
CvSeq_float_2_swigregister(CvSeq_float_2)

def CvSeq_float_2_cast(*args):
  """CvSeq_float_2_cast(CvSeq seq) -> CvSeq_float_2"""
  return _cv.CvSeq_float_2_cast(*args)

class CvSeq_float_3(CvSeq):
    """Proxy of C++ CvSeq_float_3 class"""
    __swig_setmethods__ = {}
    for _s in [CvSeq]: __swig_setmethods__.update(_s.__swig_setmethods__)
    __setattr__ = lambda self, name, value: _swig_setattr(self, CvSeq_float_3, name, value)
    __swig_getmethods__ = {}
    for _s in [CvSeq]: __swig_getmethods__.update(_s.__swig_getmethods__)
    __getattr__ = lambda self, name: _swig_getattr(self, CvSeq_float_3, name)
    __repr__ = _swig_repr
    def cast(*args):
        """cast(CvSeq seq) -> CvSeq_float_3"""
        return _cv.CvSeq_float_3_cast(*args)

    if _newclass:cast = staticmethod(cast)
    __swig_getmethods__["cast"] = lambda x: cast
    def __getitem__(*args):
        """__getitem__(self, int i) -> CvTuple_float_3"""
        return _cv.CvSeq_float_3___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int i, CvTuple_float_3 obj)"""
        return _cv.CvSeq_float_3___setitem__(*args)

    def append(*args):
        """append(self, CvTuple_float_3 obj)"""
        return _cv.CvSeq_float_3_append(*args)

    def pop(*args):
        """pop(self) -> CvTuple_float_3"""
        return _cv.CvSeq_float_3_pop(*args)

    def __init__(self, *args): 
        """__init__(self) -> CvSeq_float_3"""
        this = _cv.new_CvSeq_float_3(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cv.delete_CvSeq_float_3
    __del__ = lambda self : None;
CvSeq_float_3_swigregister = _cv.CvSeq_float_3_swigregister
CvSeq_float_3_swigregister(CvSeq_float_3)

def CvSeq_float_3_cast(*args):
  """CvSeq_float_3_cast(CvSeq seq) -> CvSeq_float_3"""
  return _cv.CvSeq_float_3_cast(*args)


def SendErrorToPython(*args):
  """
    SendErrorToPython(int status, char func_name, char err_msg, char file_name, 
        int line, void ?) -> int
    """
  return _cv.SendErrorToPython(*args)

def function_ptr_generator(*args):
  """function_ptr_generator() -> CvErrorCallback"""
  return _cv.function_ptr_generator(*args)

def void_ptr_generator(*args):
  """void_ptr_generator() -> void"""
  return _cv.void_ptr_generator(*args)

def void_ptrptr_generator(*args):
  """void_ptrptr_generator() -> void"""
  return _cv.void_ptrptr_generator(*args)
IPL_ALIGN_DWORD=IPL_ALIGN_4BYTES
IPL_ALIGN_QWORD=IPL_ALIGN_8BYTES
CV_MAKE_TYPE=CV_MAKETYPE
CV_IS_CONT_MAT=CV_IS_MAT_CONT
CV_HIST_TREE=CV_HIST_SPARSE
CV_TERMCRIT_NUMBER=CV_TERMCRIT_ITER
CV_SEQ_ELTYPE_PTR=CV_USRTYPE1
CV_GRAPH=CV_SEQ_KIND_GRAPH
CV_SEQ_CONTOUR=CV_SEQ_POLYGON
CV_STORAGE_WRITE_TEXT=CV_STORAGE_WRITE
CV_STORAGE_WRITE_BINARY=CV_STORAGE_WRITE
CV_NODE_INTEGER=CV_NODE_INT
CV_NODE_FLOAT=CV_NODE_REAL
CV_NODE_STRING=CV_NODE_STR
cvGetSubArr=cvGetSubRect
cvZero=cvSetZero
cvCvtScale=cvConvertScale
cvScale=cvConvertScale
cvCvtScaleAbs=cvConvertScaleAbs
cvCheckArray=cvCheckArr
cvMatMulAddEx=cvGEMM
cvMatMulAddS=cvTransform
cvT=cvTranspose
cvMirror=cvFlip
cvInv=cvInvert
cvMahalonobis=cvMahalanobis
CV_DXT_INVERSE_SCALE=CV_DXT_INV_SCALE
cvFFT=cvDFT
cvGraphFindEdge=cvFindGraphEdge
cvGraphFindEdgeByPtr=cvFindGraphEdgeByPtr
cvDrawRect=cvRectangle
cvDrawLine=cvLine
cvDrawCircle=cvCircle
cvDrawEllipse=cvEllipse
cvDrawPolyLine=cvPolyLine
CV_FONT_VECTOR0=CV_FONT_HERSHEY_SIMPLEX
CV_RGB2RGBA=CV_BGR2BGRA
CV_RGBA2RGB=CV_BGRA2BGR
CV_RGB2BGRA=CV_BGR2RGBA
CV_BGRA2RGB=CV_RGBA2BGR
CV_RGB2BGR=CV_BGR2RGB
CV_RGBA2BGRA=CV_BGRA2RGBA
CV_GRAY2RGB=CV_GRAY2BGR
CV_GRAY2RGBA=CV_GRAY2BGRA
CV_BayerBG2RGB=CV_BayerRG2BGR
CV_BayerGB2RGB=CV_BayerGR2BGR
CV_BayerRG2RGB=CV_BayerBG2BGR
CV_BayerGR2RGB=CV_BayerGB2BGR

__doc__ = """
OpenCV is the Intel Open CV library, an open source effort to provide
computer vision algorithms for standard PC hardware.

This wrapper was semi-automatically created from the C/C++ headers and therefore
contains no Python documentation. Because all identifiers are identical to their
C/C++ counterparts, you can consult the standard manuals that come with OpenCV.
"""

# this tells OpenCV not to call exit() on errors but throw a python exception instead
cvRedirectError(function_ptr_generator(), void_ptr_generator(), void_ptrptr_generator())




