certoraRun  certora/harnesses/SyndicateHarness.sol \
    certora/harnesses/MockStakeHouseUniverse.sol \
    certora/harnesses/MockStakeHouseRegistry.sol \
    certora/harnesses/MockSlotSettlementRegistry.sol \
    certora/harnesses/MocksETH.sol \
    --verify SyndicateHarness:certora/specs/Syndicate.spec \
    --cloud master \
    --optimistic_loop \
    --optimize 1 \
    --loop_iter 3 \
    --rules lastAccumulatedETHPerFreeFloatingShare_is_not_0_when_deregistered isNoLongerPartOfSyndicate_gosth_sound number_of_registered_knots_1 maps_are_sounds invariant_mul_isNoLongerPartOfSyndicate \
    --rule_sanity \
    --settings -optimisticFallback=true \
    --packages @blockswaplab=node_modules/@blockswaplab @openzeppelin=node_modules/@openzeppelin \
