.. _sampling:

imf.sampling
============

Functions enabling sampling for ``imf``'s mass functions, as well as the creation of downstream products such as star clusters.

Sampling details
----------------

``imf`` enables sampling either a total mass (``sample_mass``) or total number of masses (``sample_number``) from its mass functions via either random or optimal sampling.

Random sampling
^^^^^^^^^^^^^^^

Random sampling in ``imf`` is done by drawing samples from a uniform distribution and using the cumulative distribution function (CDF) associated with each IMF form to map them to masses. Sampling a total number of masses is straightforward: the specified number of masses is drawn. Sampling from a mass budget involves repeated draws until the total mass of the population exceeds the target mass. Once the threshold is reached, ``imf`` determines what to do based on one of its stop criteria, set with the ``stop_criterion`` keyword:

* ``'nearest'``: Include all stars drawn from an IMF (in drawing order) that bring the cumulative mass of the cluster closest to ``mcluster``. Sometimes exceeds ``mcluster``.

  * *Example:* Cluster with ``mcluster = 1000``, of which 950 :math:`M_\odot` are already included. The next three sampled stars have masses (0.2, 45, 10) :math:`M_\odot`. 995.2 :math:`M_\odot` (950 + 0.2 + 45) is closest to ``mcluster``, so the first two masses (0.2, 45) are included and 10 is excluded.  If instead the masses were (0.2, 45, 9), all three would be included and the total mass would be 1004.2.

* ``'before'``: Include all stars drawn from an IMF (in drawing order) with cumulative mass less than ``mcluster``. Never exceeds ``mcluster``.
* ``'after'``: Include all stars drawn from an IMF (in drawing order) with cumulative mass less than ``mcluster``, and also the next star. Always exceeds ``mcluster``.
* ``'sorted'``: Sort the stars by mass, then include or exclude massive stars based on the ``'nearest'`` criterion.

Optimal sampling
^^^^^^^^^^^^^^^^

Optimal sampling creates a population that perfectly reproduces the shape of its underlying mass function. ``imf`` implements the algorithm of `Schulz et al. (2015) <https://doi.org/10.1051/0004-6361/201425296>`__. The total mass budget and IMF are used to find the mass of the most massive star in the cluster and the accompanying scale factor for the IMF.  Successive members are added by locating the :math:`dm` along the scaled IMF that produce a :math:`dn` of 1.  This process is repeated until the entire mass budget is consumed. A total mass budget is necessary for the algorithm; if optimal sampling is called from ``sample_number``, a mass budget of :math:`N` times the provided mass function's average will be used. Generally speaking, this means that the sampled number will differ from the requested number by a small amount.

.. automodule::	sampling
   :members:	
