<template>
  <h1>Hekk</h1>
</template>
<script>
export default {
  props: ["datav"],
  created() {
    console.log(this.datav);
  }
};
</script>