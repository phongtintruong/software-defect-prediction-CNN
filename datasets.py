from collections import namedtuple
from pathlib import Path

# Dataset and results root directory
_DATASET_ROOT = Path(__file__).parent / 'data/source file'
_RESULTS_ROOT = Path(__file__).parent / 'data/labeled data'
_MAP_ROOT = Path(__file__).parent / 'data/mapped data'
_RESULTS_ROOT.mkdir(exist_ok=True)

Dataset = namedtuple('Dataset', ['name', 'root', 'versions', 'src', 'labeldata', 'mapdata'])

# Source codes and bug repositories
# DP-CNN use camel, jEdit, lucene, xalan, xerces, synapse, poi
camel = Dataset(
    'camel',
    _DATASET_ROOT / 'camel',
    [1.4, 1.6],
    [_DATASET_ROOT / 'camel/camel-1.4', _DATASET_ROOT / 'camel/camel-1.6'],
    [_RESULTS_ROOT / 'camel/camel-1.4.csv', _RESULTS_ROOT / 'camel/camel-1.6.csv'],
    [_MAP_ROOT / 'camel/camel-1.4.csv', _MAP_ROOT / 'camel/camel-1.6.csv']
)

jedit = Dataset(
    'jedit',
    _DATASET_ROOT / 'jedit',
    [4.0, 4.1],
    [_DATASET_ROOT / 'jedit/jedit-4.0', _DATASET_ROOT / 'jedit/jedit-4.1'],
    [_RESULTS_ROOT / 'jedit/jedit-4.0.csv', _RESULTS_ROOT / 'jedit/jedit-4.1.csv'],
    [_MAP_ROOT / 'jedit/jedit-4.0.csv', _MAP_ROOT / 'jedit/jedit-4.1.csv']
)

lucene = Dataset(
    'lucene',
    _DATASET_ROOT / 'lucene',
    [2.0, 2.2],
    [_DATASET_ROOT / 'lucene/lucene-2.0', _DATASET_ROOT / 'lucene/lucene-2.2'],
    [_RESULTS_ROOT / 'lucene/lucene-2.0.csv', _RESULTS_ROOT / 'lucene/lucene-2.2.csv'],
    [_MAP_ROOT / 'lucene/lucene-2.0.csv', _MAP_ROOT / 'lucene/lucene-2.2.csv']
)

xalan = Dataset(
    'xalan',
    _DATASET_ROOT / 'xalan',
    [2.5, 2.6],
    [_DATASET_ROOT / 'xalan/xalan-2.5', _DATASET_ROOT / 'xalan/xalan-2.6'],
    [_RESULTS_ROOT / 'xalan/xalan-2.5.csv', _RESULTS_ROOT / 'xalan/xalan-2.6.csv'],
    [_MAP_ROOT / 'xalan/xalan-2.5.csv', _MAP_ROOT / 'xalan/xalan-2.6.csv']
)

xerces = Dataset(
    'xerces',
    _DATASET_ROOT / 'xerces',
    [1.2, 1.3],
    [_DATASET_ROOT / 'xerces/xerces-1.2', _DATASET_ROOT / 'xerces/xerces-1.3'],
    [_RESULTS_ROOT / 'xerces/xerces-1.2.csv', _RESULTS_ROOT / 'xerces/xerces-1.3.csv'],
    [_MAP_ROOT / 'xerces/xerces-1.2.csv', _MAP_ROOT / 'xerces/xerces-1.3.csv']
)

synapse = Dataset(
    'synapse',
    _DATASET_ROOT / 'synapse',
    [1.1, 1.2],
    [_DATASET_ROOT / 'synapse/synapse-1.1', _DATASET_ROOT / 'synapse/synapse-1.2'],
    [_RESULTS_ROOT / 'synapse/synapse-1.1.csv', _RESULTS_ROOT / 'synapse/synapse-1.2.csv'],
    [_MAP_ROOT / 'synapse/synapse-1.1.csv', _MAP_ROOT / 'synapse/synapse-1.2.csv']
)

poi = Dataset(
    'poi',
    _DATASET_ROOT / 'poi',
    [2.5, 3.0],
    [_DATASET_ROOT / 'poi/poi-2.5', _DATASET_ROOT / 'poi/poi-3.0'],
    [_RESULTS_ROOT / 'poi/poi-2.5.csv', _RESULTS_ROOT / 'poi/poi-3.0.csv'],
    [_MAP_ROOT / 'poi/poi-2.5.csv', _MAP_ROOT / 'poi/poi-3.0.csv']
)

# Current dataset in use. (change this name to change the dataset)
DATASET = camel



#data after concat will be save to file CSV
_INPUT_ROOT = Path(__file__).parent / 'datainput'

Datainput = namedtuple('Datainput',['name', 'root', 'version', 'label', 'tradgene'])

savecamel = Datainput(
    'camel',
    _INPUT_ROOT / 'camel',
    [1.4, 1.6],
    [_INPUT_ROOT / 'camel/label/camel-1.4.csv', _INPUT_ROOT / 'camel/label/camel-1.6.csv'],
    [_INPUT_ROOT / 'camel/tradgene/camel-1.4.csv', _INPUT_ROOT / 'camel/tradgene/camel-1.6.csv']
)

savejedit = Datainput(
    'jedit',
    _INPUT_ROOT / 'jedit',
    [4.0, 4.1],
    [_INPUT_ROOT / 'jedit/label/jedit-4.0.csv', _INPUT_ROOT / 'jedit/label/jedit-4.1.csv'],
    [_INPUT_ROOT / 'jedit/tradgene/jedit-4.0.csv', _INPUT_ROOT / 'camel/tradgene/jedit-4.1.csv']
)

savelucene = Datainput(
    'lucene',
    _INPUT_ROOT / 'lucene',
    [2.0, 2.2],
    [_INPUT_ROOT / 'lucene/label/lucene-2.0.csv', _INPUT_ROOT / 'lucene/label/lucene-2.2.csv'],
    [_INPUT_ROOT / 'lucene/tradgene/lucene-2.0.csv', _INPUT_ROOT / 'lucene/tradgene/lucene-2.2.csv']
)

savexalan = Datainput(
    'xalan',
    _INPUT_ROOT / 'xalan',
    [2.5, 2.6],
    [_INPUT_ROOT / 'xalan/label/xalan-2.5.csv', _INPUT_ROOT / 'xalan/label/xalan-2.5.csv'],
    [_INPUT_ROOT / 'xalan/tradgene/xalan-2.5.csv', _INPUT_ROOT / 'xalan/tradgene/xalan-2.5.csv']
)

savecxerces = Datainput(
    'xerces',
    _INPUT_ROOT / 'xerces',
    [1.2, 1.3],
    [_INPUT_ROOT / 'xerces/label/xerces-1.2.csv', _INPUT_ROOT / 'xerces/label/xerces-1.3.csv'],
    [_INPUT_ROOT / 'xerces/tradgene/xerces-1.2.csv', _INPUT_ROOT / 'xerces/tradgene/xerces-1.3.csv']
)

savesynapse = Datainput(
    'synapse',
    _INPUT_ROOT / 'synapse',
    [1.1, 1.2],
    [_INPUT_ROOT / 'synapse/label/synapse-1.1.csv', _INPUT_ROOT / 'synapse/label/synapse-1.2.csv'],
    [_INPUT_ROOT / 'synapse/tradgene/synapse-1.1.csv', _INPUT_ROOT / 'synapse/tradgene/synapse-1.2.csv']
)

savepoi = Datainput(
    'poi',
    _INPUT_ROOT / 'poi',
    [2.5, 3.0],
    [_INPUT_ROOT / 'poi/label/poi-2.5.csv', _INPUT_ROOT / 'pot/label/poi-3.0.csv'],
    [_INPUT_ROOT / 'poi/tradgene/poi-2.5.csv', _INPUT_ROOT / 'poi/tradgene/poi-3.0.csv']
)



if __name__ == '__main__':

    print(savecamel.label)