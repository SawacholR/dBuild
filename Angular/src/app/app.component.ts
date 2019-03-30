import {Component, ViewChild, OnInit} from '@angular/core';
import {ModalDirective} from 'angular-bootstrap-md';
import {FormControl} from '@angular/forms';
import { Http } from '@angular/http';
import { jsonpFactory } from '@angular/http/src/http_module';
import { template } from '@angular/core/src/render3';

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"]
})
export class AppComponent {
  @ViewChild(ModalDirective) modal: ModalDirective;
  constructor(private http: Http) {}
  timeInput = new FormControl();
  subjectInput = new FormControl();
  locationInput = new FormControl();
  descriptionInput = new FormControl();
  appData = [];
  pos = [];
  neg = [];
  date = [];
  temp = 1;
  ready = false;

  chartType: string = 'line';

  chartDatasets: Array<any> = []

  public chartLabels: Array<any> = []

  public chartColors: Array<any> = [
    {
      backgroundColor: 'rgba(0, 137, 132, .2)',
      borderColor: 'rgba(0, 10, 130, .7)',
      borderWidth: 2,
    },
    {
      backgroundColor: 'rgba(105, 0, 132, .2)',
      borderColor: 'rgba(200, 99, 132, .7)',
      borderWidth: 2,
    }
  ];

  // public chartOptions: any = {
  //   responsive: true,
  //     scales: {
  //       xAxes: [{
  //         stacked: true
  //         }],
  //       yAxes: [
  //       {
  //         stacked: true
  //       }
  //     ]
  //   }
  // };

  public chartOptions: any = {
    responsive: true
  };

  public chartClicked(e: any): void { }
  public chartHovered(e: any): void { }

  events: Array<any> = [
    {time: '08:00', subject: 'Breakfast with Simon', location: 'Lounge Caffe', description: 'Discuss Q3 targets'},
    {time: '08:30', subject: 'Daily Standup Meeting (recurring)', location: 'Warsaw Spire Office'},
    {time: '09:00', subject: 'Call with HRs'},
    {time: '12:00', subject: 'Lunch with Timmoty', location: 'Canteen', description: 'Project evalutation ile declaring a variable and using an if statement is a fine way to conditionally render a component, sometimes you might want to use a'},
  ];

  public ngOnInit(): void
  {
    this.http.get('http://localhost:8000/api/getAppdata').subscribe(
      (res) => {
        this.appData = res.json();
        console.log(this.appData);
      })

    this.http.get('http://localhost:8000/api/getSentiment').subscribe(
      (res) => {
        for(let element of res.json()) {
          console.log(element.positive)
          // this.temp = +element.positive + +element.negative;
          this.pos.push(element.positive/this.temp);
          this.neg.push(element.negative/this.temp);
          this.chartLabels.push(element.date)
        }
        
        this.chartDatasets = [
          {data: this.pos, label: "Positive sentiment"},
          {data: this.neg, label: "Negative sentiment"}
        ]

        this.ready = true;
      })    
  }

  deleteEvent(event: any) {
    const itemIndex = this.events.findIndex(el => el === event);
    this.events.splice(itemIndex, 1);
  }

  addNewEvent() {
    const newEvent: any = {
      time: this.timeInput.value,
      subject: this.subjectInput.value,
      location: this.locationInput.value,
      description: this.descriptionInput.value
    };
  
    this.events.push(newEvent);
  
    this.timeInput.setValue('');
    this.subjectInput.setValue('');
    this.locationInput.setValue('');
    this.descriptionInput.setValue('');
  
    this.modal.hide();
  }
}

