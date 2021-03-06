/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package modelo;

import java.io.Serializable;
import java.util.List;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.OneToMany;
import javax.persistence.Table;

/**
 *
 * @author adelson
 */
@Entity
@Table(name = "tipo_solicitacao_delegacao")
public class TipoSolicitacaoDelegacao implements Serializable {
    
    @Id
    private long id;
    
    @Column(length = 80)
    private String nome;
    
    @Column(length = 300)
    private String descricao;
    
    @Enumerated(EnumType.STRING)
    @Column(length = 12)
    private tipo.TipoSolicitacaoDelegacao tipo;
    
    @ManyToMany(fetch = FetchType.EAGER)
    @JoinTable(name = "tipo_solicitacao_delegacao_item", 
            joinColumns = {@JoinColumn(name = "tipo_solicitacao_delegacao_id")}, 
            inverseJoinColumns = {@JoinColumn(name = "tipo_item_id")})
    private List<TipoItem> tipoItens;
    
    

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public tipo.TipoSolicitacaoDelegacao getTipo() {
        return tipo;
    }

    public void setTipo(tipo.TipoSolicitacaoDelegacao tipo) {
        this.tipo = tipo;
    }

    public List<TipoItem> getTipoItens() {
        return tipoItens;
    }

    public void setTipoItens(List<TipoItem> tipoItens) {
        this.tipoItens = tipoItens;
    }

    
}
