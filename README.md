Distance to agreement calculations for radiotherapy dose distributions
======================================================================

Currently an n-dimensional version of gamma evaluation is the only algorithm implemented. The resolution in the sample and reference can be difference, however each axis of in sample and reference respectively must be the sample resolution.

    from dta import gamma_evaluation
    
    distance = 3                        # 3 mm
    threshold = reference.max()*0.03    # 3 % of max in reference
    sample_res, reference_res = (2, 1)  # 2 mm voxels in sample, 1 mm in ref

    gamma_map = gamma_evaluation(sample, reference,
                                 distance, threshold,
                                 (sample_res, reference_res))

