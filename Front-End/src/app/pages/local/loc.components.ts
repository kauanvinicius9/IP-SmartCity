import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { LocalService } from '../../services/local.services';
import { Local } from '../../models/local';
import { AuthService } from '../../services/auth.services';
import { environment } from '../../../environments/environments';

@Component({
  selector: 'app-local',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './local.components.html',
})
export class LocalComponent {
  private svc = inject(LocalService);
  private auth = inject(AuthService);

  local = signal<Local[]>([]);
  carregando = signal(true);
  erro = signal<string | null>(null);

  apiBase = (environment.apiBase ?? '').replace(/\/+$/, '');

  private pendentes = new Map<number, File>();
  private previews = new Map<number, string>();
  private upStatus = new Map<number, 'idle' | 'up' | 'ok' | 'err'>();

  constructor() {
    this.carregarLocais();
  }
  private carregarLocais() {
    this.svc.listar().subscribe({
        next: (data) => {
            this.local.set(data);
            this.carregando.set(false);
        },
        error: (err) => {
            this.erro.set('Erro ao carregar locais');
            this.carregando.set(false)
        },
     });
  }
  
}