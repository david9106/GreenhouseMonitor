<<<<<<< HEAD
||||||| merged common ancestors
function mergeJSON(source1,source2){
    /*
     * Properties from the Souce1 object will be copied to Source2 Object.
     * Note: This method will return a new merged object, Source1 and Source2 original values will not be replaced.
     * */
    var mergedJSON = Object.create(source2);// Copying Source2 to a new Object
	
	///Change "attrname" by date property, since it's the one that we want to ignore in case that it already exists
=======
function mergeJSON(source1,source2){
    /**
     * Properties from the Souce1 object will be copied to Source2 Object.
     * Note: This method will return a new merged object, Source1 and Source2 original values will not be replaced.
     */
    var mergedJSON = Object.create(source2);// Copying Source2 to a new Object
	
	///Change "attrname" by date property, since it's the one that we want to ignore in case that it already exists
>>>>>>> doxygen

