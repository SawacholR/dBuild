import {Component, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-details',
  templateUrl: './app-details.html',
})
export class EventComponent {
    @Input() value: any;
    @Output() deleteEventInstanceEvent: EventEmitter<any> = new EventEmitter<any>();

    handleDeleteClick() {
        this.deleteEventInstanceEvent.emit(this.value);
      }
} 