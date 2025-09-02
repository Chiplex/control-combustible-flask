document.addEventListener('DOMContentLoaded', function() {
    // Autocomplete functionality
    class AutoComplete {
        constructor(inputId, suggestionsId, hiddenInputId, apiUrl, displayProperty, searchProperties, valueProperty) {
            this.input = document.getElementById(inputId);
            this.suggestions = document.getElementById(suggestionsId);
            this.hiddenInput = document.getElementById(hiddenInputId);
            this.apiUrl = apiUrl;
            this.displayProperty = displayProperty;
            this.searchProperties = searchProperties;
            this.valueProperty = valueProperty;
            this.selectedIndex = -1;
            this.data = [];
            
            this.init();
        }
        
        init() {
            this.input.addEventListener('input', (e) => this.handleInput(e));
            this.input.addEventListener('keydown', (e) => this.handleKeydown(e));
            this.input.addEventListener('focus', () => this.showSuggestions());
            document.addEventListener('click', (e) => this.handleOutsideClick(e));
            
            // Load initial data
            this.loadData();
        }
        
        async loadData() {
            try {
                const response = await fetch(this.apiUrl);
                this.data = await response.json();
            } catch (error) {
                console.error('Error loading data:', error);
            }
        }
        
        handleInput(e) {
            const query = e.target.value.toLowerCase();
            this.hiddenInput.value = ''; // Clear hidden input when typing
            this.filterAndShowSuggestions(query);
        }
        
        handleKeydown(e) {
            const suggestions = this.suggestions.querySelectorAll('.autocomplete-suggestion');
            
            switch(e.key) {
                case 'ArrowDown':
                    e.preventDefault();
                    this.selectedIndex = Math.min(this.selectedIndex + 1, suggestions.length - 1);
                    this.updateSelection(suggestions);
                    break;
                    
                case 'ArrowUp':
                    e.preventDefault();
                    this.selectedIndex = Math.max(this.selectedIndex - 1, -1);
                    this.updateSelection(suggestions);
                    break;
                    
                case 'Enter':
                    e.preventDefault();
                    if (this.selectedIndex >= 0 && suggestions[this.selectedIndex]) {
                        this.selectSuggestion(suggestions[this.selectedIndex]);
                    }
                    break;
                    
                case 'Escape':
                    this.hideSuggestions();
                    break;
            }
        }
        
        handleOutsideClick(e) {
            if (!e.target.closest('.autocomplete-container')) {
                this.hideSuggestions();
            }
        }
        
        filterAndShowSuggestions(query) {
            const filtered = this.data.filter(item => {
                return this.searchProperties.some(prop => {
                    const value = this.getNestedProperty(item, prop);
                    return value && value.toLowerCase().includes(query);
                });
            });
            
            this.showSuggestionsList(filtered);
        }
        
        showSuggestions() {
            if (this.input.value.length === 0) {
                this.showSuggestionsList(this.data.slice(0, 10)); // Show first 10 items
            }
        }
        
        showSuggestionsList(items) {
            this.suggestions.innerHTML = '';
            this.selectedIndex = -1;
            
            if (items.length === 0) {
                this.suggestions.innerHTML = '<div class="autocomplete-suggestion">No se encontraron resultados</div>';
                this.suggestions.style.display = 'block';
                return;
            }
            
            items.forEach((item, index) => {
                const div = document.createElement('div');
                div.className = 'autocomplete-suggestion';
                div.innerHTML = this.formatSuggestion(item);
                div.addEventListener('click', () => this.selectSuggestion(div));
                div.dataset.index = index;
                div.dataset.value = this.getNestedProperty(item, this.valueProperty);
                
                this.suggestions.appendChild(div);
            });
            
            this.suggestions.style.display = 'block';
        }
        
        formatSuggestion(item) {
            // Override this method in subclasses for custom formatting
            return this.getNestedProperty(item, this.displayProperty);
        }
        
        selectSuggestion(suggestionDiv) {
            const value = suggestionDiv.dataset.value;
            const text = suggestionDiv.textContent;
            
            this.input.value = text;
            this.hiddenInput.value = value;
            this.hideSuggestions();
        }
        
        updateSelection(suggestions) {
            suggestions.forEach((suggestion, index) => {
                suggestion.classList.toggle('selected', index === this.selectedIndex);
            });
        }
        
        hideSuggestions() {
            this.suggestions.style.display = 'none';
            this.selectedIndex = -1;
        }
        
        getNestedProperty(obj, path) {
            return path.split('.').reduce((o, p) => o && o[p], obj);
        }
    }
    
    // Custom AutoComplete for tanks
    class TankAutoComplete extends AutoComplete {
        formatSuggestion(item) {
            return `<span class="code">${item.Codigo}</span> <span class="details">(${item.Tipo})</span>`;
        }
    }
    
    // Custom AutoComplete for responsables
    class ResponsableAutoComplete extends AutoComplete {
        formatSuggestion(item) {
            return `<span class="code">${item.Nombre}</span> <span class="details">CI: ${item.CI}</span>`;
        }
    }
    
    // Initialize autocomplete fields
    if (document.getElementById('tanque_destino_search')) {
        new TankAutoComplete(
            'tanque_destino_search',
            'tanque_destino_suggestions', 
            'tanque_destino_id',
            '/api/tanques/Consumo',
            'Codigo',
            ['Codigo'],
            'TanqueId'
        );
    }
    
    if (document.getElementById('responsable_search')) {
        new ResponsableAutoComplete(
            'responsable_search',
            'responsable_suggestions',
            'responsable_id', 
            '/api/responsables',
            'Nombre',
            ['Nombre', 'CI'],
            'ResponsableId'
        );
    }
});