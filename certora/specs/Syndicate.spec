using MocksETH as sETHToken

methods {
    //// Regular methods
    //totalETHReceived() returns (uint256) envfree
    //isKnotRegistered(bytes32) returns (bool) envfree

    //// Resolving external calls
	// stakeHouseUniverse
	stakeHouseKnotInfo(bytes32) returns (address,address,address,uint256,uint256,bool) => DISPATCHER(true)
    memberKnotToStakeHouse(bytes32) returns (address) => DISPATCHER(true) // not used directly by Syndicate
    // stakeHouseRegistry
    getMemberInfo(bytes32) returns (address,uint256,uint16,bool) => DISPATCHER(true) // not used directly by Syndicate
    // slotSettlementRegistry
	stakeHouseShareTokens(address) returns (address)  => DISPATCHER(true)
	currentSlashedAmountOfSLOTForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	numberOfCollateralisedSlotOwnersForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	getCollateralisedOwnerAtIndex(bytes32, uint256) returns (address) => DISPATCHER(true)
	totalUserCollateralisedSLOTBalanceForKnot(address, address, bytes32) returns (uint256) => DISPATCHER(true)
    // sETH
    sETHToken.balanceOf(address) returns (uint256) envfree
    // ERC20
    name()                                returns (string)  => DISPATCHER(true)
    symbol()                              returns (string)  => DISPATCHER(true)
    decimals()                            returns (string) envfree => DISPATCHER(true)
    totalSupply()                         returns (uint256) => DISPATCHER(true)
    balanceOf(address)                    returns (uint256) => DISPATCHER(true)
    allowance(address,address)            returns (uint)    => DISPATCHER(true)
    approve(address,uint256)              returns (bool)    => DISPATCHER(true)
    transfer(address,uint256)             returns (bool)    => DISPATCHER(true)
    transferFrom(address,address,uint256) returns (bool)    => DISPATCHER(true)

    //// Harnessing
    // harnessed variables
//    accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32,address) returns (uint256) envfree
//    totalETHProcessedPerCollateralizedKnot(bytes32) returns (uint256) envfree
//    sETHStakedBalanceForKnot(bytes32,address) returns (uint256) envfree
//    sETHTotalStakeForKnot(bytes32) returns (uint256) envfree
    // harnessed functions
    deRegisterKnots(bytes32) 
    deRegisterKnots(bytes32,bytes32)
    stake(bytes32,uint256,address)
    stake(bytes32,bytes32,uint256,uint256,address)
    unstake(address,address,bytes32,uint256)
    unstake(address,address,bytes32,bytes32,uint256,uint256)
    claimAsStaker(address,bytes32)
    claimAsStaker(address,bytes32,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32,bytes32)
    registerKnotsToSyndicate(bytes32)
    registerKnotsToSyndicate(bytes32,bytes32)
    addPriorityStakers(address)
    addPriorityStakers(address,address)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32, bytes32)
    // envfree funcs
    /* These are public storage value from the contract, so envfree */
    accumulatedETHPerFreeFloatingShare() returns (uint256) envfree;
    accumulatedETHPerCollateralizedSlotPerKnot() returns (uint256) envfree;
    lastSeenETHPerCollateralizedSlotPerKnot() returns (uint256) envfree;
    lastSeenETHPerFreeFloating() returns (uint256) envfree;
    totalFreeFloatingShares() returns (uint256) envfree;
    totalClaimed() returns (uint256) envfree;
    numberOfRegisteredKnots() returns (uint256) envfree;
    isKnotRegistered(bytes32) returns (bool) envfree;
    priorityStakingEndBlock() returns (uint256) envfree;
    isPriorityStaker(address) returns (bool) envfree;
    sETHTotalStakeForKnot(bytes32) returns (uint256) envfree;
    sETHStakedBalanceForKnot(bytes32, address) returns (uint256) envfree;
    sETHUserClaimForKnot(bytes32, address) returns (uint256) envfree;
    totalETHProcessedPerCollateralizedKnot(bytes32) returns (uint256) envfree;
    accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32, address) returns (uint256) envfree;
    claimedPerCollateralizedSlotOwnerOfKnot(bytes32, address) returns (uint256) envfree;
    isNoLongerPartOfSyndicate(bytes32) returns (bool) envfree;
    lastAccumulatedETHPerFreeFloatingShare(bytes32) returns (uint256) envfree;
    updateAccruedETHPerSharesWasCalled() returns (bool) envfree;
    PRECISION() returns (uint256) envfree;
}

/// We defined additional functions to get around the complexity of defining dynamic arrays in cvl. We filter them in 
/// normal rules and invariants as they serve no purpose.
definition notHarnessCall(method f) returns bool = 
    f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32).selector
    && f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32).selector
    && f.selector != deRegisterKnots(bytes32).selector
    && f.selector != deRegisterKnots(bytes32,bytes32).selector
    && f.selector != stake(bytes32,uint256,address).selector
    && f.selector != stake(bytes32,bytes32,uint256,uint256,address).selector
    && f.selector != unstake(address,address,bytes32,uint256).selector
    && f.selector != unstake(address,address,bytes32,bytes32,uint256,uint256).selector
    && f.selector != claimAsStaker(address,bytes32).selector
    && f.selector != claimAsStaker(address,bytes32,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32,bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32,bytes32).selector
    && f.selector != addPriorityStakers(address).selector
    && f.selector != addPriorityStakers(address,address).selector;

/// Filters out method that involves arrays, and use harness methods instead
definition OnlyHarnessCallWhenNeeded(method f) returns bool = 
    f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32[]).selector
    && f.selector != deRegisterKnots(bytes32[]).selector
    && f.selector != stake(bytes32[],uint256[],address).selector
    && f.selector != unstake(address,address,bytes32[],uint256[]).selector
    && f.selector != claimAsStaker(address,bytes32[]).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32[]).selector
    && f.selector != registerKnotsToSyndicate(bytes32[]).selector
    && f.selector != addPriorityStakers(address[]).selector;

/// Filters out harness methods that are arrays with 2 elements to prevent timeouts
definition OnlySingleArgumentCall(method f) returns bool =
    f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32).selector
    && f.selector != deRegisterKnots(bytes32).selector
    && f.selector != stake(bytes32,uint256,address).selector
    && f.selector != unstake(address,address,bytes32,uint256).selector
    && f.selector != claimAsStaker(address,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32).selector
    && f.selector != addPriorityStakers(address).selector
    // remove function that batch calls
    && f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32[]).selector
    && f.selector != batchPreviewUnclaimedETHAsFreeFloatingStaker(address, bytes32[]).selector
    && f.selector != batchPreviewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32[]).selector;

/// Remove all the variant of the stake function
definition NotStake(method f) returns bool =
    f.selector != stake(bytes32,uint256,address).selector
    && f.selector != stake(bytes32,bytes32,uint256,uint256,address).selector
    && f.selector != stake(bytes32[],uint256[],address).selector;

/**
 * An unregistered knot can not be deregistered.
 */
// ok
rule canNotDegisterUnregisteredKnot(method f) filtered {
    f -> notHarnessCall(f)
} {
    bytes32 knot; env e;
    require !isKnotRegistered(knot);

    deRegisterKnots@withrevert(e, knot);

    assert lastReverted, "deRegisterKnots must revert if knot is not registered";
}

/**
 * Total ETH received must not decrease.
 */
// ok
rule totalEthReceivedMonotonicallyIncreases(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    uint256 totalEthReceivedBefore = totalETHReceived(e);

    calldataarg args;
    f(e, args);

    uint256 totalEthReceivedAfter = totalETHReceived(e);

    assert totalEthReceivedAfter >= totalEthReceivedBefore, "total ether received must not decrease";
}

/* If someone else than you make a call to the contract, then your balances can only increases */
// ok
rule noOneCanAlterTheMoneyYouHave(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    bytes32 blsPubKey;
    uint256 amount;
    address staker;
    require currentContract != staker;

    uint realEthAmountBefore = sETHToken.balanceOf(staker);
    uint256 sETHAmountBefore = sETHStakedBalanceForKnot(blsPubKey, staker);
    
    calldataarg args;
    f(e, args);

    uint realEthAmountAfter = sETHToken.balanceOf(staker);
    uint256 sETHAmountAfter = sETHStakedBalanceForKnot(blsPubKey, staker);

    assert sETHAmountAfter + realEthAmountAfter < sETHAmountBefore + realEthAmountBefore => e.msg.sender == staker, "The total amount of money you have need to be at least what you had before";
}

/* Same, but more money kept track of */
// todo
rule noOneCanAlterTheMoneyYouHave_2(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    bytes32 blsPubKey;
    uint256 amount;
    address staker;
    require currentContract != staker;

    uint256 money1_before = sETHToken.balanceOf(staker);
    uint256 money2_before = sETHStakedBalanceForKnot(blsPubKey, staker);
    uint256 money3_before = sETHUserClaimForKnot(blsPubKey, staker);
    uint256 money4_before = accruedEarningPerCollateralizedSlotOwnerOfKnot(blsPubKey, staker);
    uint256 money5_before = claimedPerCollateralizedSlotOwnerOfKnot(blsPubKey, staker);
    
    calldataarg args;
    f(e, args);

    uint256 money1_after = sETHToken.balanceOf(staker);
    uint256 money2_after = sETHStakedBalanceForKnot(blsPubKey, staker);
    uint256 money3_after = sETHUserClaimForKnot(blsPubKey, staker);
    uint256 money4_after = accruedEarningPerCollateralizedSlotOwnerOfKnot(blsPubKey, staker);
    uint256 money5_after = claimedPerCollateralizedSlotOwnerOfKnot(blsPubKey, staker);

    assert ((money1_before > money1_after) ||
        (money2_before > money2_after) ||
        (money3_before > money3_after) ||
        (money4_before > money4_after) ||
        (money5_before != money5_after)) => e.msg.sender == staker,
    "The money 'about you' shouldn't change with someone else call";
}

/* When you stake, you can immediatly unstake and get back your money */
// Wanted to write "every call to unstake for sure reverts", but failed
// So the rule written here is not really what I had in mind
rule stakeThenUnstake() {

    env e;
    bytes32 blsPubKey;
    uint256 sETHAmounts;
    address staker = e.msg.sender;
    require currentContract != staker;

    requireInvariant addressZeroHasNoBalance();

    requireInvariant both_sum_are_sound();

    requireInvariant sETHSolvency();

    requireInvariant totalStakeAmount(blsPubKey);

    requireInvariant isNoLongerPartOfSyndicate_gosth_sound(blsPubKey);

    requireInvariant number_of_registered_knots_1();

    requireInvariant maps_are_sounds();

    require numberOfRegisteredKnots() > 0;
    require sETHAmounts > 0;

    stake(e, blsPubKey, sETHAmounts, staker);
    unstake(e, staker, staker, blsPubKey, sETHAmounts);

    assert true, "You should be able to unstake immediatly after staking";
}

/* Simple withdraw */
// Catch bug1
// Ok otherwise
rule simpleWithdraw() {

    env e;
    bytes32 blsPubKey;
    address staker;
    uint realEthAmountBefore = sETHToken.balanceOf(staker);
    uint contractbalanceBefore = sETHToken.balanceOf(currentContract);
    uint256 sETHAmount;
    
    unstake(e, staker, staker, blsPubKey, sETHAmount);

    uint realEthAmountAfter = sETHToken.balanceOf(staker);
    uint contractbalanceAfter = sETHToken.balanceOf(currentContract);

    assert (realEthAmountAfter == realEthAmountBefore + sETHAmount) &&
        (contractbalanceBefore - sETHAmount == contractbalanceAfter),
    "Simple withdraw";
}

/* You can always withdraw what you have in sETHStakedBalanceForKnot, and get your money back */
/* Huge fail
definition MAXINT() returns uint256 = 0xffffffffffffffffffffff;
rule canAlwaysWithdraw() {

    env e;
    bytes32 blsPubKey;
    address staker = e.msg.sender;
    require(staker != currentContract);
    uint256 sETHAmount;
    


    requireInvariant addressZeroHasNoBalance();

    requireInvariant both_sum_are_sound();

    requireInvariant sETHSolvency();

    requireInvariant totalStakeAmount(blsPubKey);

    requireInvariant isNoLongerPartOfSyndicate_gosth_sound(blsPubKey);

    requireInvariant number_of_registered_knots_1();

    requireInvariant maps_are_sounds();

    require(e.msg.value == 0);
    require(staker != 0);
    require(isKnotRegistered(blsPubKey));
    require(sETHStakedBalanceForKnot(blsPubKey, e.msg.sender) >= sETHAmount);

    // Prevent overflow in computation of unstake
    // These value probably can't be reached anyway (todo write it?)
    require(sETHAmount <= MAXINT()); // Why not
    // +
    require(totalClaimed() <= MAXINT());
    // -
    require(totalFreeFloatingShares() >= sETHAmount);
    require(sETHTotalStakeForKnot(blsPubKey) >= sETHAmount);
    require(sETHStakedBalanceForKnot(blsPubKey, staker) >= sETHAmount);
    require(totalETHReceived(e)/2 >= lastSeenETHPerCollateralizedSlotPerKnot());
    // *
    require(lastAccumulatedETHPerFreeFloatingShare(blsPubKey) <= MAXINT());
    require(sETHStakedBalanceForKnot(blsPubKey, staker) <= MAXINT());
    // /
    require(numberOfRegisteredKnots() <= MAXINT());
    // +=
    require(accumulatedETHPerCollateralizedSlotPerKnot() <= MAXINT());
    // useless
    require(lastSeenETHPerCollateralizedSlotPerKnot() <= MAXINT());
    // ensure subcall to calculateUnclaimedFreeFloatingETHShare does not revert
    uint256 userShare = (lastAccumulatedETHPerFreeFloatingShare(blsPubKey) * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION();
    require(sETHUserClaimForKnot(blsPubKey, staker) <= MAXINT());
    require(userShare >= sETHUserClaimForKnot(blsPubKey, staker));

    currentContract.pauseNonreentrancy(e); // Todo make it env free
    unstake@withrevert(e, staker, staker, blsPubKey, sETHAmount);
    bool reverted = lastReverted;
    assert !reverted;
}
*/

/* Cannot registered a knot if he is already registered */
rule canNotDegisterUnregisteredKnot() {
    bytes32 knot; env e;
    require isKnotRegistered(knot);

    registerKnotsToSyndicate@withrevert(e, knot);

    assert lastReverted, "registerKnotsToSyndicate must revert if knot is already registered";
}

// bool to uint256
function conv (bool arg) returns uint256 {
    if (arg) return 1;
    else return 0;
}
// Functions that pick element from the state
/* Except what update... is responssible of modifying:
accumulatedETHPerFreeFloatingShare
lastSeenETHPerFreeFloating
accumulatedETHPerCollateralizedSlotPerKnot
lastSeenETHPerCollateralizedSlotPerKnot
*/
function randomElementFromStateNoUpdateAccruedETHPerShares(uint256 select, bytes32 bytes32_arg, address address_arg) returns uint256 {
    uint256 answer = 0;
    //if (select == 0) answer = accumulatedETHPerFreeFloatingShare();
    //if (select == 1) answer = accumulatedETHPerCollateralizedSlotPerKnot();
    //if (select == 2) answer = lastSeenETHPerCollateralizedSlotPerKnot();
    //if (select == 3) answer = lastSeenETHPerFreeFloating();
    if (select == 4) answer = totalFreeFloatingShares();
    if (select == 5) answer = totalClaimed();
    if (select == 6) answer = numberOfRegisteredKnots();
    if (select == 7) answer = conv(isKnotRegistered(bytes32_arg));
    if (select == 8) answer = priorityStakingEndBlock();
    if (select == 9) answer = conv(isPriorityStaker(address_arg));
    if (select == 10) answer = sETHTotalStakeForKnot(bytes32_arg);
    if (select == 11) answer = sETHStakedBalanceForKnot(bytes32_arg, address_arg);
    if (select == 12) answer = sETHUserClaimForKnot(bytes32_arg, address_arg);
    if (select == 13) answer = totalETHProcessedPerCollateralizedKnot(bytes32_arg);
    if (select == 14) answer = accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32_arg, address_arg);
    if (select == 15) answer = claimedPerCollateralizedSlotOwnerOfKnot(bytes32_arg, address_arg);
    if (select == 16) answer = conv(isNoLongerPartOfSyndicate(bytes32_arg));
    if (select == 17) answer = lastAccumulatedETHPerFreeFloatingShare(bytes32_arg);
    return answer;
}
function randomElementFromState(uint256 select, bytes32 bytes32_arg, address address_arg) returns uint256 {
    uint256 answer = 0;
    if (select == 0) answer = accumulatedETHPerFreeFloatingShare();
    if (select == 1) answer = accumulatedETHPerCollateralizedSlotPerKnot();
    if (select == 2) answer = lastSeenETHPerCollateralizedSlotPerKnot();
    if (select == 3) answer = lastSeenETHPerFreeFloating();
    if (select == 4) answer = totalFreeFloatingShares();
    if (select == 5) answer = totalClaimed();
    if (select == 6) answer = numberOfRegisteredKnots();
    if (select == 7) answer = conv(isKnotRegistered(bytes32_arg));
    if (select == 8) answer = priorityStakingEndBlock();
    if (select == 9) answer = conv(isPriorityStaker(address_arg));
    if (select == 10) answer = sETHTotalStakeForKnot(bytes32_arg);
    if (select == 11) answer = sETHStakedBalanceForKnot(bytes32_arg, address_arg);
    if (select == 12) answer = sETHUserClaimForKnot(bytes32_arg, address_arg);
    if (select == 13) answer = totalETHProcessedPerCollateralizedKnot(bytes32_arg);
    if (select == 14) answer = accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32_arg, address_arg);
    if (select == 15) answer = claimedPerCollateralizedSlotOwnerOfKnot(bytes32_arg, address_arg);
    if (select == 16) answer = conv(isNoLongerPartOfSyndicate(bytes32_arg));
    if (select == 17) answer = lastAccumulatedETHPerFreeFloatingShare(bytes32_arg);
    return answer;
}

/* If you want to stake to 2 blspubkeys, then you get the same result if you split your function call into 2 calls
So stake([key1, key2], ...) and stake(key1, ...); stake(key2, ...) gives the same result */
// Timeout
rule ruleArrayStake() {

    env e;
    uint256 select;
    bytes32 bytes32_arg;
    address address_arg;

    bytes32 blsPubKey1;
    bytes32 blsPubKey2;
    uint256 sETHAmount1;
    uint256 sETHAmount2;
    address staker;

    bytes32 arg_blsPubKey;
    address arg_staker;

    // To reduce a bit the TO
    require address_arg == staker;
    require (bytes32_arg == blsPubKey1) || (bytes32_arg == blsPubKey2);

    requireInvariant maps_are_sounds();
    requireInvariant number_of_registered_knots_1();
    requireInvariant both_sum_are_sound();
    updateAccruedETHPerShares(e);

    storage startState = lastStorage;
    stake(e, blsPubKey1, sETHAmount1, staker);
    stake(e, blsPubKey2, sETHAmount2, staker);
    updateAccruedETHPerShares(e);
    uint256 value1 = randomElementFromStateNoUpdateAccruedETHPerShares(select, bytes32_arg, address_arg);
    
    stake(e, blsPubKey1, blsPubKey2, sETHAmount1, sETHAmount2, staker) at startState;
    updateAccruedETHPerShares(e);
    uint256 value2 = randomElementFromStateNoUpdateAccruedETHPerShares(select, bytes32_arg, address_arg);

    assert value1 == value2, "If someone splits a stake calls into multiple then it shouldn't change the result!";
}

/* Only the staking action can be reverted by the priority staking
aka you can still unstake even if the owner go rogue and change the priority staking to an absurd value */
// Some rules here timeout
rule rugpullPriorityStakingCanRevert(method f) filtered {
    f -> (OnlyHarnessCallWhenNeeded(f) && NotStake(f))
}{

    env e;
    calldataarg args;
    uint rugpullBlockNumber;

    updateAccruedETHPerShares(e);
    uint startBlockNumber = e.block.number;
    storage startState = lastStorage;

    f@withrevert(e, args);
    bool reverted1 = lastReverted;

    updatePriorityStakingBlock(e, rugpullBlockNumber) at startState;
    require(e.block.number == startBlockNumber);
    f@withrevert(e, args);
    bool reverted2 = lastReverted;

    assert reverted1 == reverted2,
        "Only stake can be changed by priority staking. Nothing else. Owner cannot rug and prevent you from withdrawing by changing the starting block";
}

/* Assuming both call revert on the same arguments (proven above), then they give the same result!
So same, owner cannot rug */
rule rugpullPriorityStakingSameResult(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    uint rugpullBlockNumber;

    uint256 select;
    require(select != 8); // select=8 returns priorityStakingEndBlock, the variable we modify with updatePriorityStakingBlock
    bytes32 bytes32_arg;
    address address_arg;

    uint startBlockNumber;
    storage startState = lastStorage;

    updateAccruedETHPerShares(e); // Because updateprioritystaker calls it, so to get the same result we need to call it too
    require(e.block.number == startBlockNumber);
    f(e, args);
    uint256 value1 = randomElementFromState(select, bytes32_arg, address_arg);

    updatePriorityStakingBlock(e, rugpullBlockNumber) at startState;
    require(e.block.number == startBlockNumber);
    f(e, args);
    uint256 value2 = randomElementFromState(select, bytes32_arg, address_arg);

    assert value1 == value2,
        "If the call hasn't revert, then changing the priority block number shouldn't change the result";
}





/* State variables that are modified by updateAccruedETHPerShares cannot be accessed without going through this function with numberOfRegisteredKnots!=0 */
/* So you can't complete a call that will read these variables, and having went through this function OR went throught this function but had numberOfRegisteredKnots==0 */

/* First, 2 bool gosth that takes the value 1 if any of these variable are read/written to */
/* The variables we are interested in are:
accumulatedETHPerFreeFloatingShare
lastSeenETHPerFreeFloating
accumulatedETHPerCollateralizedSlotPerKnot
lastSeenETHPerCollateralizedSlotPerKnot
*/
ghost bool read_statevar_of_updateAccruedETHPerShares;
ghost bool write_statevar_of_updateAccruedETHPerShares;

hook Sstore accumulatedETHPerFreeFloatingShare uint256 v STORAGE { write_statevar_of_updateAccruedETHPerShares = true; }
hook Sstore lastSeenETHPerFreeFloating uint256 v STORAGE { write_statevar_of_updateAccruedETHPerShares = true; }
hook Sstore accumulatedETHPerCollateralizedSlotPerKnot uint256 v STORAGE { write_statevar_of_updateAccruedETHPerShares = true; }
hook Sstore lastSeenETHPerCollateralizedSlotPerKnot uint256 v STORAGE { write_statevar_of_updateAccruedETHPerShares = true; }

hook Sload uint256 v accumulatedETHPerFreeFloatingShare STORAGE { read_statevar_of_updateAccruedETHPerShares = true; }
hook Sload uint256 v lastSeenETHPerFreeFloating STORAGE { read_statevar_of_updateAccruedETHPerShares = true; }
hook Sload uint256 v accumulatedETHPerCollateralizedSlotPerKnot STORAGE { read_statevar_of_updateAccruedETHPerShares = true; }
hook Sload uint256 v lastSeenETHPerCollateralizedSlotPerKnot STORAGE { read_statevar_of_updateAccruedETHPerShares = true; }


/* Cannot make it work
rule cannotReadStateVariablesWithoutCallToUpdate(method f) {
    env e;
    calldataarg args;
    require(!updateAccruedETHPerSharesWasCalled());
    require(!read_statevar_of_updateAccruedETHPerShares);
    requireInvariant maps_are_sounds();
    requireInvariant number_of_registered_knots_1();
    f(e, args);
    assert read_statevar_of_updateAccruedETHPerShares => updateAccruedETHPerSharesWasCalled(),
    "Cannot read variables related to updateAccruedETHPerShares without going throught the function";
}
*/
/* Only some function can written some storage value */
// ok
rule cannotWriteStateVariablesWithoutCallToUpdate(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    require(!updateAccruedETHPerSharesWasCalled());
    require(!write_statevar_of_updateAccruedETHPerShares);
    f(e, args);
    assert write_statevar_of_updateAccruedETHPerShares => updateAccruedETHPerSharesWasCalled(),
    "Cannot write variables related to updateAccruedETHPerShares without going throught the function";
}

/* Todo, these variables can't be written by another function than update... */

/************************************************************************************************ INVARIANTS ***********************************************************************************************/

/* ... */
invariant addressZeroHasNoBalance()
    sETHToken.balanceOf(0) == 0

ghost mathint sum_sETHStakedBalanceForKnot {
    init_state axiom sum_sETHStakedBalanceForKnot == 0;
}
ghost mathint sum_sETHStakedBalanceForKnot_liveonly {
    init_state axiom sum_sETHStakedBalanceForKnot_liveonly == 0;
}
hook Sstore sETHStakedBalanceForKnot[KEY bytes32 blsPubKey][KEY address staker] uint256 new_value (uint256 old_value) STORAGE {
    sum_sETHStakedBalanceForKnot = sum_sETHStakedBalanceForKnot + new_value - old_value;
    sum_sETHStakedBalanceForKnot_liveonly = sum_sETHStakedBalanceForKnot_liveonly + (isNoLongerPartOfSyndicate_gosth[blsPubKey] ? 0 : (new_value - old_value));
}
ghost mathint sum_sETHTotalStakeForKnot {
    init_state axiom sum_sETHTotalStakeForKnot == 0;
}
hook Sstore sETHTotalStakeForKnot[KEY bytes32 blsPubKey] uint256 new_value (uint256 old_value) STORAGE {
    sum_sETHTotalStakeForKnot = sum_sETHTotalStakeForKnot + new_value - old_value;
}

/* sum(sETHTotalStakeForKnot[key]) == sum(sum(sETHStakedBalanceForKnot[key][user])) */
// ok
invariant both_sum_are_sound()
    sum_sETHStakedBalanceForKnot == sum_sETHTotalStakeForKnot

/* The balance of the contract is always above what is kept track of */
// ok
invariant sETHSolvency()
    sETHToken.balanceOf(currentContract) >= sum_sETHTotalStakeForKnot
    { preserved with (env e) { require e.msg.sender != currentContract; } }

/* Stacked amount cannot be more than 12eth */
// ok
invariant totalStakeAmount(bytes32 blsPubKey)
    sETHTotalStakeForKnot(blsPubKey) <= 12000000000000000000



/* Calculate functions */


/* lastAccumulatedETHPerFreeFloatingShare is only used when isNoLongerPartOfSyndicate is true */
// ok
invariant lastAccumulatedETHPerFreeFloatingShare_is_0_unless_deregistered(bytes32 blsPubKey)
    lastAccumulatedETHPerFreeFloatingShare(blsPubKey) != 0 => isNoLongerPartOfSyndicate(blsPubKey)

/* And the reverse, if isNoLongerPartOfSyndicate is true, then lastAccumulatedETHPerFreeFloatingShare is used */
// ok, but with a patch in the code line 662
invariant lastAccumulatedETHPerFreeFloatingShare_is_not_0_when_deregistered(bytes32 blsPubKey)
    isNoLongerPartOfSyndicate(blsPubKey) => lastAccumulatedETHPerFreeFloatingShare(blsPubKey) != 0


/************************************************************************************************ GOSTHS ***********************************************************************************************/

ghost mathint number_of_registered_knots {
    init_state axiom number_of_registered_knots == 0;
}
ghost mathint number_of_deregistered_knots {
    init_state axiom number_of_deregistered_knots == 0;
}
ghost bool both_maps_are_sound {
    init_state axiom both_maps_are_sound == false;
}
ghost mapping(bytes32 => bool) isNoLongerPartOfSyndicate_gosth {
    init_state axiom forall bytes32 blsPubKey. isNoLongerPartOfSyndicate_gosth[blsPubKey] == false;
}

/* isNoLongerPartOfSyndicate_gosth is a correct gosth of isNoLongerPartOfSyndicate */
// ok
invariant isNoLongerPartOfSyndicate_gosth_sound(bytes32 blsPubKey)
    isNoLongerPartOfSyndicate_gosth[blsPubKey] => isNoLongerPartOfSyndicate(blsPubKey)

hook Sstore isNoLongerPartOfSyndicate[KEY bytes32 blsPubKey] bool new_value (bool old_value) STORAGE {
    number_of_deregistered_knots = number_of_deregistered_knots + 1;
    both_maps_are_sound = ((!new_value) || old_value) ? true : false;
    isNoLongerPartOfSyndicate_gosth[blsPubKey] = true;
}
hook Sstore isKnotRegistered[KEY bytes32 blsPubKey] bool new_value (bool old_value) STORAGE {
    number_of_registered_knots = number_of_registered_knots + 1;
    both_maps_are_sound = ((!new_value) || old_value) ? true : false;
}

/* sum(isKnotRegistered) - sum(isNoLongerPartOfSyndicate) == numberOfRegisteredKnots */
// ok
invariant number_of_registered_knots_1()
    number_of_registered_knots - number_of_deregistered_knots == numberOfRegisteredKnots()

/* When te 2 maps isKnotRegistered and isNoLongerPartOfSyndicate are written, it's always from false to true */
// ok
invariant maps_are_sounds()
    both_maps_are_sound == false


/* sETHUserClaimForKnot verifies some equation when isNoLongerPartOfSyndicate(blsPubKey) */
// ok
rule invariant_mul_isNoLongerPartOfSyndicate(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    bytes32 blsPubKey;
    address staker;
    require isKnotRegistered(blsPubKey);
    require isNoLongerPartOfSyndicate(blsPubKey);
    requireInvariant lastAccumulatedETHPerFreeFloatingShare_is_not_0_when_deregistered(blsPubKey);
    updateAccruedETHPerShares(e);
    require sETHUserClaimForKnot(blsPubKey, staker) == (lastAccumulatedETHPerFreeFloatingShare(blsPubKey) * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION();
    f(e, args);
    assert sETHUserClaimForKnot(blsPubKey, staker) == (lastAccumulatedETHPerFreeFloatingShare(blsPubKey) * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION(),
    "Total free floating share is sound if some invariant is assumed";
}

/* lastAccumulatedETHPerFreeFloatingShare cannot changed once a knot has been deregistered */
// ok
rule lastAccumulatedETHPerFreeFloatingShareCannotChangeOnceDeregistered(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    bytes32 blsPubKey;
    address staker;
    require isKnotRegistered(blsPubKey);
    require isNoLongerPartOfSyndicate(blsPubKey);
    uint startValue = lastAccumulatedETHPerFreeFloatingShare(blsPubKey);
    f(e, args);
    uint endValue = lastAccumulatedETHPerFreeFloatingShare(blsPubKey);
    assert startValue == endValue, "Value snapshotted when deregistration cannot be changed!";
}

/* sETHUserClaimForKnot verifies some equation when !isNoLongerPartOfSyndicate(blsPubKey) */
// I believe it should be ok but I get I believe a rounding/1-off error
rule sETHUsETHUserClaimForKnot_sound(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    bytes32 blsPubKey;
    address staker;
    require isKnotRegistered(blsPubKey);
    require !isNoLongerPartOfSyndicate(blsPubKey);
    updateAccruedETHPerShares(e);
    require sETHUserClaimForKnot(blsPubKey, staker) == (accumulatedETHPerFreeFloatingShare() * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION();
    f(e, args);
    require !isNoLongerPartOfSyndicate(blsPubKey);
    assert sETHUserClaimForKnot(blsPubKey, staker) == (accumulatedETHPerFreeFloatingShare() * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION(),
    "Total free floating share is sound if some invariant is assumed";
}

/* sETHUserClaimForKnot verifies the same equation, but always! */
// Same rounding error
rule completeInvariant(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    bytes32 blsPubKey;
    address staker;
    require isKnotRegistered(blsPubKey);
    requireInvariant lastAccumulatedETHPerFreeFloatingShare_is_not_0_when_deregistered(blsPubKey);
    updateAccruedETHPerShares(e);
    uint256 startValue = !isNoLongerPartOfSyndicate(blsPubKey) ? accumulatedETHPerFreeFloatingShare() : lastAccumulatedETHPerFreeFloatingShare(blsPubKey);
    require sETHUserClaimForKnot(blsPubKey, staker) == (startValue * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION();
    f(e, args);
    uint256 endValue = !isNoLongerPartOfSyndicate(blsPubKey) ? accumulatedETHPerFreeFloatingShare() : lastAccumulatedETHPerFreeFloatingShare(blsPubKey);
    assert sETHUserClaimForKnot(blsPubKey, staker) == (endValue * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION();
}


// But no more than 1?
// ok
rule imprecisionIsBounded(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    bytes32 blsPubKey;
    address staker;
    require isKnotRegistered(blsPubKey);
    require isNoLongerPartOfSyndicate(blsPubKey);
    requireInvariant lastAccumulatedETHPerFreeFloatingShare_is_not_0_when_deregistered(blsPubKey);
    updateAccruedETHPerShares(e);
    uint256 a = sETHUserClaimForKnot(blsPubKey, staker);
    uint256 b = (lastAccumulatedETHPerFreeFloatingShare(blsPubKey) * sETHStakedBalanceForKnot(blsPubKey, staker)) / PRECISION();
    require ((a-b <= 1) && (b-a <= 1));
    f(e, args);
    assert ((a-b <= 1) && (b-a <= 1)),
    "Impression cannot be more than 1?";
}

/* The rounding error cannot be more than 1, not very sure this rule tests that correctly */
// ok
rule impressisionIsBounded(method f) filtered {
    f -> notHarnessCall(f)
}{
    env e;
    calldataarg args;
    bytes32 blsPubKey;
    address staker;
    require isKnotRegistered(blsPubKey);
    require !isNoLongerPartOfSyndicate(blsPubKey);
    updateAccruedETHPerShares(e);
    /* BEFORE */
    uint256 a = !isNoLongerPartOfSyndicate(blsPubKey) ? accumulatedETHPerFreeFloatingShare() : lastAccumulatedETHPerFreeFloatingShare(blsPubKey);
    mathint math_a = a;
    uint256 b = sETHStakedBalanceForKnot(blsPubKey, staker);
    mathint math_b = b;
    uint256 c = PRECISION();
    mathint math_c = c;
    uint256 res = sETHUserClaimForKnot(blsPubKey, staker);
    mathint math_res = res;
    // a, b, and c are free to take whatever value they want as long as the computation gives the result that "is stored" by the smart contract
    require (a*b)/c == res;
    // However, the difference between the value stored by the smart contract (res), and the computation done at each step (a*b/c) may grow
    // This difference is
    mathint difference_before = math_res - (math_a * math_b) / math_c;
    //differenceBefore = differenceBefore < 0 ? -differenceBefore : differenceBefore;
    require difference_before <= PRECISION();
    // Let's do a random call, and see if the difference can grow
    f(e, args);
    /* AFTER */
    uint256 a_after = !isNoLongerPartOfSyndicate(blsPubKey) ? accumulatedETHPerFreeFloatingShare() : lastAccumulatedETHPerFreeFloatingShare(blsPubKey);
    mathint math_a_after = a;
    uint256 b_after = sETHStakedBalanceForKnot(blsPubKey, staker);
    mathint math_b_after = b;
    uint256 c_after = PRECISION();
    mathint math_c_after = c;
    uint256 res_after = sETHUserClaimForKnot(blsPubKey, staker);
    mathint math_res_after = res;
    // a, b, and c are free to take whatever value they want as long as the computation gives the result that "is stored" by the smart contract
    //require (a*b)/c == res;
    // However, the difference between the value stored by the smart contract (res), and the computation done at each step (a*b/c) may grow
    // This difference is
    mathint difference_after = math_res_after - (math_a_after * math_b_after) / math_c_after;
    //difference_after = difference_after < 0 ? -difference_after : difference_after;
    assert difference_after <= PRECISION(), "Impression cannot grow above precision";
}
