from collections import OrderedDict
from unittest import TestCase

import yaml

import yamlloader

config1 = """name: sim1_all_result
model:
  categories:
  - Mode
  pdf:
    rare:
      sig:
        yield: VAR 10000 0 1000000
        brem0:
          yield: VAR 0.5 0 1
          mass:
            observable-names:
              mass: B_M
            pdf: cb
            mass_limits:
              low: 5000
              high: 6000.0
            parameters:
              mu: VAR 5279 5250 5300
              sigma: VAR 14.53 2 100
              alpha: VAR 1.097 0.001 4
              n: VAR 1.73 0.00001 150
        brem1:
          yield: VAR 0.5 0 1
          mass:
            observable-names:
              mass: B_M
            pdf: doublecb
            mass_limits:
              low: 5000
              high: 6000
            parameters:
              mu: VAR 5279 5250 5300
              sigma1: VAR 14.53 2 100
              alpha1: VAR 1.097 0.001 4
              n1: VAR 1.73 0.00001 150
              sigma2: VAR 14.53 2 100
              alpha2: VAR -1.097 -4 -0.001
              n2: VAR 1.73 0.00001 150
              frac: VAR 0.5 0 1
        brem2:
          mass:
            observable-names:
              mass: B_M
            pdf: doublecb
            mass_limits:
              low: 5000
              high: 6000
            parameters:
              shift1: '@shift1/shift1/shift1/VAR 1. 0.5 1.5'
              mu_fixed: '@muTrue/muTrue/muTrue/CONST 5279'
              mu: SHIFT @muTrue @shift1
              sigma1: VAR 14.53 2 100
              alpha1: VAR 1.097 0.001 4
              n1: VAR 1.73 0.00001 150
              sigma2: VAR 14.53 2 100
              alpha2: VAR -1.097 -4 -0.001
              n2: VAR 1.73 0.00001 150
              frac: VAR 0.5 0.3 0.7
      comb_bkg:
        yield: VAR 4000 0 10000
        mass:
          observable-names:
            mass: B_M
          pdf: exponential
          mass_limits:
            low: 5000
            high: 6000
          parameters:
            tau: VAR -0.0008 -0.1 -0.0001
      part_bkg:
        yield: VAR 40000 10000 1000000
        mass:
          observable-names:
            mass: B_M
          pdf: gaussian
          mass_limits:
            low: 5000
            high: 5400
          parameters:
            mu: VAR 5100 5001 5100
            sigma: VAR 10 0 10000
    jpsi:
      sig:
        yield: VAR 10000 0 1000000
        brem0:
          yield: VAR 0.5 0 1
          mass:
            observable-names:
              mass: B_M
            pdf: cb
            mass_limits:
              low: 5000
              high: 6000.0
            parameters:
              mu: VAR 5279 5250 5300
              sigma: VAR 14.53 2 100
              alpha: VAR 1.097 0.001 4
              n: VAR 1.73 0.00001 150
        brem1:
          yield: VAR 0.5 0 1
          mass:
            observable-names:
              mass: B_M
            pdf: doublecb
            mass_limits:
              low: 5000
              high: 6000
            parameters:
              mu: VAR 5279 5250 5300
              sigma1: VAR 14.53 2 100
              alpha1: VAR 1.097 0.001 4
              n1: VAR 1.73 0.00001 150
              sigma2: VAR 14.53 2 100
              alpha2: VAR -1.097 -4 -0.001
              n2: VAR 1.73 0.00001 150
              frac: VAR 0.5 0 1
        brem2:
          mass:
            observable-names:
              mass: B_M
            pdf: doublecb
            mass_limits:
              low: 5000
              high: 6000
            parameters:
              mu: SHIFT @muTrue @shift1
              sigma1: VAR 14.53 2 100
              alpha1: VAR 1.097 0.001 4
              n1: VAR 1.73 0.00001 150
              sigma2: VAR 14.53 2 100
              alpha2: VAR -1.097 -4 -0.001
              n2: VAR 1.73 0.00001 150
              frac: VAR 0.5 0.3 0.7
      comb_bkg:
        yield: VAR 4000 0 10000
        mass:
          observable-names:
            mass: B_M
          pdf: exponential
          mass_limits:
            low: 5000
            high: 6000
          parameters:
            tau: VAR -0.0008 -0.1 -0.0001
      part_bkg:
        yield: VAR 40000 10000 1000000
        mass:
          observable-names:
            mass: B_M
          pdf: gaussian
          mass_limits:
            low: 5000
            high: 5400
          parameters:
            mu: VAR 5100 5001 5100
            sigma: VAR 10 0 10000
"""

config1_target = OrderedDict(
    [
        ("name", "sim1_all_result"),
        (
            "model",
            OrderedDict(
                [
                    ("categories", ["Mode"]),
                    (
                        "pdf",
                        OrderedDict(
                            [
                                (
                                    "rare",
                                    OrderedDict(
                                        [
                                            (
                                                "sig",
                                                OrderedDict(
                                                    [
                                                        (
                                                            "yield",
                                                            "VAR 10000 " "0 1000000",
                                                        ),
                                                        (
                                                            "brem0",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "yield",
                                                                        "VAR 0.5 0 1",
                                                                    ),
                                                                    (
                                                                        "mass",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "observable-names",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mass",
                                                                                                "B_M",
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "pdf",
                                                                                    "cb",
                                                                                ),
                                                                                (
                                                                                    "mass_limits",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "low",
                                                                                                5000,
                                                                                            ),
                                                                                            (
                                                                                                "high",
                                                                                                6000.0,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "parameters",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mu",
                                                                                                "VAR 5279 5250 5300",
                                                                                            ),
                                                                                            (
                                                                                                "sigma",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha",
                                                                                                "VAR 1.097 0.001 4",
                                                                                            ),
                                                                                            (
                                                                                                "n",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                        (
                                                            "brem1",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "yield",
                                                                        "VAR 0.5 0 1",
                                                                    ),
                                                                    (
                                                                        "mass",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "observable-names",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mass",
                                                                                                "B_M",
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "pdf",
                                                                                    "doublecb",
                                                                                ),
                                                                                (
                                                                                    "mass_limits",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "low",
                                                                                                5000,
                                                                                            ),
                                                                                            (
                                                                                                "high",
                                                                                                6000,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "parameters",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mu",
                                                                                                "VAR 5279 5250 5300",
                                                                                            ),
                                                                                            (
                                                                                                "sigma1",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha1",
                                                                                                "VAR 1.097 0.001 4",
                                                                                            ),
                                                                                            (
                                                                                                "n1",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "sigma2",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha2",
                                                                                                "VAR -1.097 -4 -0.001",
                                                                                            ),
                                                                                            (
                                                                                                "n2",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "frac",
                                                                                                "VAR 0.5 0 1",
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                        (
                                                            "brem2",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "mass",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "observable-names",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mass",
                                                                                                "B_M",
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "pdf",
                                                                                    "doublecb",
                                                                                ),
                                                                                (
                                                                                    "mass_limits",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "low",
                                                                                                5000,
                                                                                            ),
                                                                                            (
                                                                                                "high",
                                                                                                6000,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "parameters",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "shift1",
                                                                                                "@shift1/shift1/shift1/VAR 1. 0.5 1.5",
                                                                                            ),
                                                                                            (
                                                                                                "mu_fixed",
                                                                                                "@muTrue/muTrue/muTrue/CONST 5279",
                                                                                            ),
                                                                                            (
                                                                                                "mu",
                                                                                                "SHIFT @muTrue @shift1",
                                                                                            ),
                                                                                            (
                                                                                                "sigma1",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha1",
                                                                                                "VAR 1.097 0.001 4",
                                                                                            ),
                                                                                            (
                                                                                                "n1",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "sigma2",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha2",
                                                                                                "VAR -1.097 -4 -0.001",
                                                                                            ),
                                                                                            (
                                                                                                "n2",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "frac",
                                                                                                "VAR 0.5 0.3 0.7",
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    )
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "comb_bkg",
                                                OrderedDict(
                                                    [
                                                        (
                                                            "yield",
                                                            "VAR 4000 " "0 10000",
                                                        ),
                                                        (
                                                            "mass",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "observable-names",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "mass",
                                                                                    "B_M",
                                                                                )
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "pdf",
                                                                        "exponential",
                                                                    ),
                                                                    (
                                                                        "mass_limits",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "low",
                                                                                    5000,
                                                                                ),
                                                                                (
                                                                                    "high",
                                                                                    6000,
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "parameters",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "tau",
                                                                                    "VAR -0.0008 -0.1 -0.0001",
                                                                                )
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "part_bkg",
                                                OrderedDict(
                                                    [
                                                        (
                                                            "yield",
                                                            "VAR 40000 "
                                                            "10000 "
                                                            "1000000",
                                                        ),
                                                        (
                                                            "mass",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "observable-names",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "mass",
                                                                                    "B_M",
                                                                                )
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    ("pdf", "gaussian"),
                                                                    (
                                                                        "mass_limits",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "low",
                                                                                    5000,
                                                                                ),
                                                                                (
                                                                                    "high",
                                                                                    5400,
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "parameters",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "mu",
                                                                                    "VAR 5100 5001 5100",
                                                                                ),
                                                                                (
                                                                                    "sigma",
                                                                                    "VAR 10 0 10000",
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "jpsi",
                                    OrderedDict(
                                        [
                                            (
                                                "sig",
                                                OrderedDict(
                                                    [
                                                        (
                                                            "yield",
                                                            "VAR 10000 " "0 1000000",
                                                        ),
                                                        (
                                                            "brem0",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "yield",
                                                                        "VAR 0.5 0 1",
                                                                    ),
                                                                    (
                                                                        "mass",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "observable-names",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mass",
                                                                                                "B_M",
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "pdf",
                                                                                    "cb",
                                                                                ),
                                                                                (
                                                                                    "mass_limits",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "low",
                                                                                                5000,
                                                                                            ),
                                                                                            (
                                                                                                "high",
                                                                                                6000.0,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "parameters",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mu",
                                                                                                "VAR 5279 5250 5300",
                                                                                            ),
                                                                                            (
                                                                                                "sigma",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha",
                                                                                                "VAR 1.097 0.001 4",
                                                                                            ),
                                                                                            (
                                                                                                "n",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                        (
                                                            "brem1",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "yield",
                                                                        "VAR 0.5 0 1",
                                                                    ),
                                                                    (
                                                                        "mass",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "observable-names",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mass",
                                                                                                "B_M",
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "pdf",
                                                                                    "doublecb",
                                                                                ),
                                                                                (
                                                                                    "mass_limits",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "low",
                                                                                                5000,
                                                                                            ),
                                                                                            (
                                                                                                "high",
                                                                                                6000,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "parameters",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mu",
                                                                                                "VAR 5279 5250 5300",
                                                                                            ),
                                                                                            (
                                                                                                "sigma1",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha1",
                                                                                                "VAR 1.097 0.001 4",
                                                                                            ),
                                                                                            (
                                                                                                "n1",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "sigma2",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha2",
                                                                                                "VAR -1.097 -4 -0.001",
                                                                                            ),
                                                                                            (
                                                                                                "n2",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "frac",
                                                                                                "VAR 0.5 0 1",
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                        (
                                                            "brem2",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "mass",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "observable-names",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mass",
                                                                                                "B_M",
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "pdf",
                                                                                    "doublecb",
                                                                                ),
                                                                                (
                                                                                    "mass_limits",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "low",
                                                                                                5000,
                                                                                            ),
                                                                                            (
                                                                                                "high",
                                                                                                6000,
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                (
                                                                                    "parameters",
                                                                                    OrderedDict(
                                                                                        [
                                                                                            (
                                                                                                "mu",
                                                                                                "SHIFT @muTrue @shift1",
                                                                                            ),
                                                                                            (
                                                                                                "sigma1",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha1",
                                                                                                "VAR 1.097 0.001 4",
                                                                                            ),
                                                                                            (
                                                                                                "n1",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "sigma2",
                                                                                                "VAR 14.53 2 100",
                                                                                            ),
                                                                                            (
                                                                                                "alpha2",
                                                                                                "VAR -1.097 -4 -0.001",
                                                                                            ),
                                                                                            (
                                                                                                "n2",
                                                                                                "VAR 1.73 0.00001 150",
                                                                                            ),
                                                                                            (
                                                                                                "frac",
                                                                                                "VAR 0.5 0.3 0.7",
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    )
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "comb_bkg",
                                                OrderedDict(
                                                    [
                                                        (
                                                            "yield",
                                                            "VAR 4000 " "0 10000",
                                                        ),
                                                        (
                                                            "mass",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "observable-names",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "mass",
                                                                                    "B_M",
                                                                                )
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "pdf",
                                                                        "exponential",
                                                                    ),
                                                                    (
                                                                        "mass_limits",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "low",
                                                                                    5000,
                                                                                ),
                                                                                (
                                                                                    "high",
                                                                                    6000,
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "parameters",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "tau",
                                                                                    "VAR -0.0008 -0.1 -0.0001",
                                                                                )
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "part_bkg",
                                                OrderedDict(
                                                    [
                                                        (
                                                            "yield",
                                                            "VAR 40000 "
                                                            "10000 "
                                                            "1000000",
                                                        ),
                                                        (
                                                            "mass",
                                                            OrderedDict(
                                                                [
                                                                    (
                                                                        "observable-names",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "mass",
                                                                                    "B_M",
                                                                                )
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    ("pdf", "gaussian"),
                                                                    (
                                                                        "mass_limits",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "low",
                                                                                    5000,
                                                                                ),
                                                                                (
                                                                                    "high",
                                                                                    5400,
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "parameters",
                                                                        OrderedDict(
                                                                            [
                                                                                (
                                                                                    "mu",
                                                                                    "VAR 5100 5001 5100",
                                                                                ),
                                                                                (
                                                                                    "sigma",
                                                                                    "VAR 10 0 10000",
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
)

text_target_odict = [(config1, config1_target)]


class TestLoaderDumper(TestCase):
    def set_LoadersDumpers(self, loader, dumper):
        self.loader = loader
        self.dumper = dumper

    def test_ordereddict(self):
        self.set_LoadersDumpers(
            yamlloader.ordereddict.CLoader, dumper=yamlloader.ordereddict.CDumper
        )
        for yaml_file, yaml_target in text_target_odict:
            self.loaddump(dict_to_save=yaml_target, dump_target=yaml_file)

    def loaddump(self, dict_to_save, dump_target=None, loader=None, dumper=None):
        if loader is None:
            loader = self.loader
        if dumper is None:
            dumper = self.dumper
        dumped_dict = yaml.dump(dict_to_save, Dumper=dumper, default_flow_style=False)
        if dump_target:
            self.assertEqual(dumped_dict, dump_target)
        dict_loaded = yaml.load(dumped_dict, Loader=loader)
        self.assertEqual(dict_to_save, dict_loaded)
