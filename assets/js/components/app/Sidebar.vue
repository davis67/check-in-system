<script>
export default {
  data() {
    return {
      showProfileDropdown: false
    };
  },
  methods: {
    toggleProfileDropdown() {
      console.log(!this.showProfileDropdown);
      this.showProfileDropdown = !this.showProfileDropdown;
    }
  },
  created() {
    console.log("log");
  }
};
</script>