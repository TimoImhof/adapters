import unittest
from math import ceil

import pytest

from tests.test_impl.composition.test_parallel import ParallelAdapterInferenceTestMixin, ParallelTrainingMixin
from tests.test_impl.core.test_adapter_backward_compability import CompabilityTestMixin
from tests.test_impl.core.test_adapter_conversion import ModelClassConversionTestMixin
from tests.test_impl.core.test_adapter_fusion_common import AdapterFusionModelTestMixin
from tests.test_impl.embeddings.test_adapter_embeddings import EmbeddingTestMixin
from tests.test_impl.heads.test_adapter_heads import PredictionHeadModelTestMixin
from tests.test_impl.peft.test_adapter_common import BottleneckAdapterTestMixin
from tests.test_impl.peft.test_compacter import CompacterTestMixin
from tests.test_impl.peft.test_config_union import ConfigUnionAdapterTest
from tests.test_impl.peft.test_ia3 import IA3TestMixin
from tests.test_impl.peft.test_lora import LoRATestMixin
from tests.test_impl.peft.test_prefix_tuning import PrefixTuningTestMixin
from tests.test_impl.peft.test_prompt_tuning import PromptTuningTestMixin
from tests.test_impl.peft.test_reft import ReftTestMixin
from tests.test_impl.peft.test_unipelt import UniPELTTestMixin
from tests.test_methods.base import TextAdapterTestBase, make_config
from transformers import AutoTokenizer
from transformers.testing_utils import require_torch