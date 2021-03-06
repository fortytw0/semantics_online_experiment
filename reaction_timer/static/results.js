var myChart = new Chart("experiment1", {
  type: "bar",
  data: {
    labels:results.username,
    datasets: [
      {
        label: 'Images Match',
        data:results.first_experiment,
        borderWidth:1, 
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)']
      }, 

      {
        label: 'Images dont match',
        data:results.second_experiment,
        borderWidth:1, 
        backgroundColor: [
          'rgba(54, 162, 235, 0.2)']
      }, 

      {
        label: 'Texts Match',
        data:results.third_experiment,
        borderWidth:1, 
        backgroundColor: [
          'rgba(255, 205, 86, 0.2)']
      },

      {
        label: 'Texts dont Unmatch',
        data:results.fourth_experiment,
        borderWidth:1, 
        backgroundColor: [
          'rgba(75, 192, 192, 0.2)']
      }
    ]
    
  },
  options: {
    scales: {
      y: {
        beginAtZero: false
      }
    }
  }
});


