from MyPackage import myModule

def test_top1_n():
    """
    make sure top _nworks correctly
    """
    assert myModule.top_n([8,3,2,7,4],3) ==[8,7,4], 'incorrect'
    assert myModule.top_n([10,1,12,9,2],2) ==[12,10], 'incorrect'
    assert myModule.top_n([1,2,3,4,5],5) ==[5,4,3,2,1], 'incorrect'